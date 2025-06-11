import tkinter as tk
import json
import time

def create_window_execute(parent, steps_json, ingredients_json):
    execute_window = tk.Toplevel(parent)  # Κατασκευή Toplevel widget που έχει ως parent το root widget (κυρίως παράθυρο)
    ExecuteRecipeWindow(execute_window, steps_json, ingredients_json)

import threading # Εξήγηση: https://www.geeksforgeeks.org/how-to-use-thread-in-tkinter-python/

class ExecuteRecipeWindow:
    def __init__(self, master, steps_json, ingredients_json):
        self.master = master
        self.master.title("Execute Recipe")
        self.steps = json.loads(steps_json)
        self.ingredients = json.loads(ingredients_json)
        self.current_index = 0
        self.timer_running = False
        self.timer_paused = False
        self.remaining_time = 0
        self.timer_thread = None

        # Συνολικός χρόνος
        total_time = self.calculate_total_time()
        tk.Label(master, text=f"Total Estimated Time: {total_time} min").pack(pady=5)

        # Λίστα βημάτων
        tk.Label(master, text=f"Execution Steps").pack(pady=5)
        self.step_summary = tk.Listbox(master, width=60)
        for idx, step in enumerate(self.steps):
            summary = f"{idx+1}. {step['description'][:30]}... ({step['time']})"
            self.step_summary.insert(tk.END, summary)
        self.step_summary.pack(pady=5)

        # Λίστα υλικών
        tk.Label(master, text=f"Ingredients").pack(pady=5)
        self.ingredient_summary = tk.Listbox(master, width=60)
        for idx, ingredient in enumerate(self.ingredients):
            summary = f"{idx+1}. {ingredient['name'][:30]}: ({ingredient['quantity']})"
            self.ingredient_summary.insert(tk.END, summary)
        self.ingredient_summary.pack(pady=5)

        # Εκτύπωση βήματος
        self.step_label = tk.Label(master, text="", wraplength=500, justify="left")
        self.step_label.pack(pady=10)

        # Αντίστροφη μέτρηση
        self.timer_label = tk.Label(master, text="", font=("Helvetica", 16))
        self.timer_label.pack(pady=5)

        # Control buttons
        button_frame = tk.Frame(master)
        button_frame.pack(pady=10)

        self.start_btn = tk.Button(button_frame, text="▶ Start", command=self.start_timer)
        self.start_btn.grid(row=0, column=0, padx=5)

        self.pause_btn = tk.Button(button_frame, text="⏸ Pause", command=self.pause_timer)
        self.pause_btn.grid(row=0, column=1, padx=5)

        self.resume_btn = tk.Button(button_frame, text="▶ Resume", command=self.resume_timer)
        self.resume_btn.grid(row=0, column=2, padx=5)

        self.prev_btn = tk.Button(button_frame, text="⏮ Prev", command=self.prev_step)
        self.prev_btn.grid(row=0, column=3, padx=5)

        self.next_btn = tk.Button(button_frame, text="⏭ Next", command=self.next_step)
        self.next_btn.grid(row=0, column=4, padx=5)

        self.load_step(self.current_index)

    def calculate_total_time(self):
        total = 0
        for step in self.steps:
            try:
                num = int((step['time']))
                total += num
            except:
                pass
        return total

    def load_step(self, index):
        if 0 <= index < len(self.steps):
            self.current_index = index
            self.step_label.config(text=self.steps[index]['description'])
            try:
                self.remaining_time = int(self.steps[index]['time'])
            except:
                self.remaining_time = 0
            self.update_timer_label()

    def update_timer_label(self):
        self.timer_label.config(text=f"{self.remaining_time} seconds remaining")

    def timer_loop(self):
        while self.remaining_time > 0 and self.timer_running and not self.timer_paused:
            time.sleep(1)
            self.remaining_time -= 1
            self.master.after(0, self.update_timer_label)

        if self.remaining_time == 0 and self.timer_running and not self.timer_paused:
            self.master.after(0, self.next_step)

    def start_timer(self):
        self.timer_running = True
        self.timer_paused = False
        self.timer_thread = threading.Thread(target=self.timer_loop)
        self.timer_thread.start()

    def pause_timer(self):
        self.timer_paused = True

    def resume_timer(self):
        if self.timer_running:
            self.timer_paused = False
            self.timer_thread = threading.Thread(target=self.timer_loop)
            self.timer_thread.start()

    def next_step(self):
        self.timer_running = False
        self.load_step(self.current_index + 1)

    def prev_step(self):
        self.timer_running = False
        self.load_step(self.current_index - 1)
