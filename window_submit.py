import tkinter as tk
from tkinter import ttk, messagebox
import handle_data
import json

CATEGORIES = ["Κρεατικά", "Ζυμαρικά/Ρύζι", "Μαγειρευτά", "Ψάρι/θαλασσινά", "Σαλάτες", "Ορεκτικά", "Έθνικ"]
DIFFICULTY_OPTIONS = ["Εύκολο", "Μέτριας δυσκολίας", "Δύσκολο"]

def create_window_submit(parent, previous_recipe=None):

    # Kaloume auto to parathyro gia na metatrepsei mia hdh yparxousa syntagh;
    # Ean nai, modify = True
    modify = False
    new_recipe = handle_data.Recipe()
    if previous_recipe == None:
        previous_recipe=handle_data.Recipe()
    else:
        new_recipe.name = previous_recipe.name
        new_recipe.category = previous_recipe.category
        new_recipe.difficulty = previous_recipe.difficulty
        new_recipe.ingredients = previous_recipe.ingredients
        new_recipe.steps = previous_recipe.steps
        modify = True

    handle_data.show_all_recipes() # debug
    ingredients = []
    steps = []

    def add_ingredient():
        name = ingredient_name_entry.get().strip()
        qty = ingredient_qty_entry.get().strip()
        if not name or not qty:
            messagebox.showwarning("Incomplete", "Please enter both name and quantity.")
            return
        ingredients.append({"name": name, "quantity": qty})
        ingredient_listbox.insert(tk.END, f"{name} - {qty}")
        ingredient_name_entry.delete(0, tk.END)
        ingredient_qty_entry.delete(0, tk.END)

    def add_step():
        desc = step_desc_entry.get().strip()
        time_val = step_time_entry.get().strip()

        if not desc or not time_val:
            messagebox.showwarning("Incomplete", "Enter both instruction and time.")
            return
        if not time_val.isdigit():
            messagebox.showerror("Invalid Time", "Step time must be a number (seconds).")
            return

        steps.append({"description": desc, "time": time_val})
        step_listbox.insert(tk.END, f"{len(steps)}. {desc[:30]}... ({time_val}s)")
        step_desc_entry.delete(0, tk.END)
        step_time_entry.delete(0, tk.END)

    def save_text():
        # Get the values fro the window elements
        entered_name = entry_name.get()
        entered_category = entry_category.get()
        entered_difficulty = entry_difficulty.get()

        if not entered_name:
            messagebox.showerror("Missing Field", "Recipe name is required.")
            return

        entrered_ingredients_json = json.dumps(ingredients, ensure_ascii=False)
        entered_steps_json = json.dumps(steps, ensure_ascii=False)

        # Define the new recipe to be saved!!
        new_recipe.name = entered_name
        new_recipe.category = entered_category
        new_recipe.difficulty = entered_difficulty
        new_recipe.ingredients = entrered_ingredients_json
        new_recipe.steps = entered_steps_json

        if modify == True:
            new_recipe.ingredients = previous_recipe.ingredients
            new_recipe.steps = previous_recipe.steps

            handle_data.delete_recipe_by_id(previous_recipe.id)

        if modify == False:
            searched_existing_recipes_by_name = handle_data.search_recipe_by_name_only(entered_name)
            if searched_existing_recipes_by_name[0].name != "":
                for found_recipe in searched_existing_recipes_by_name:
                    if found_recipe.name == entered_name:
                        messagebox.showerror("Invalid name", "A recipe with this name already exists.")
                        return

        handle_data.save_recipe_to_db(new_recipe)
        messagebox.showinfo("Saved", f"Recipe '{entered_name}' saved successfully.")
        this_window.destroy()

    this_window = tk.Toplevel(parent)
    this_window.title("Submit Recipe")
    this_window.geometry("800x900")
    this_window.resizable(False, False)

    # Recipe Info
    recipe_frame = tk.LabelFrame(this_window, text="Recipe Details", padx=10, pady=10)
    recipe_frame.pack(padx=10, pady=10, fill="x")

    tk.Label(recipe_frame, text="Recipe Name:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
    entry_name = tk.Entry(recipe_frame, width=40, textvariable=tk.StringVar(value=previous_recipe.name))
    entry_name.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(recipe_frame, text="Category:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
    entry_category = ttk.Combobox(recipe_frame, values=CATEGORIES, width=37) 
    entry_category.set(previous_recipe.category)
    entry_category.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(recipe_frame, text="Difficulty:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
    entry_difficulty = ttk.Combobox(recipe_frame, values=DIFFICULTY_OPTIONS, width=37)
    entry_difficulty.set(previous_recipe.difficulty)
    entry_difficulty.grid(row=2, column=1, padx=5, pady=5)

    # Ingredients
    ingredient_frame = tk.LabelFrame(this_window, text="Ingredients", padx=10, pady=10)
    ingredient_frame.pack(padx=10, pady=10, fill="x")

    tk.Label(ingredient_frame, text="Ingredient:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
    ingredient_name_entry = tk.Entry(ingredient_frame, width=20)
    ingredient_name_entry.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(ingredient_frame, text="Quantity:").grid(row=0, column=2, padx=5, pady=5, sticky="e")
    ingredient_qty_entry = tk.Entry(ingredient_frame, width=15)
    ingredient_qty_entry.grid(row=0, column=3, padx=5, pady=5)

    add_ingredient_btn = tk.Button(ingredient_frame, text="Add", command=add_ingredient)
    add_ingredient_btn.grid(row=0, column=4, padx=10)

    ingredient_listbox = tk.Listbox(ingredient_frame, width=60)
    ingredient_listbox.grid(row=1, column=0, columnspan=5, pady=10)

    # Execution Steps
    step_frame = tk.LabelFrame(this_window, text="Execution Steps", padx=10, pady=10)
    step_frame.pack(padx=10, pady=10, fill="x")

    tk.Label(step_frame, text="Step Instruction:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
    step_desc_entry = tk.Entry(step_frame, width=40)
    step_desc_entry.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(step_frame, text="Time (sec):").grid(row=0, column=2, padx=5, pady=5, sticky="e")
    step_time_entry = tk.Entry(step_frame, width=10)
    step_time_entry.grid(row=0, column=3, padx=5, pady=5)

    add_step_btn = tk.Button(step_frame, text="Add Step", command=add_step)
    add_step_btn.grid(row=0, column=4, padx=5)

    step_listbox = tk.Listbox(step_frame, width=80)
    step_listbox.grid(row=1, column=0, columnspan=5, pady=10)

    # Buttons
    btn_frame = tk.Frame(this_window)
    btn_frame.pack(pady=10)

    save_button = tk.Button(btn_frame, text="Save", width=15, command=save_text)
    save_button.grid(row=0, column=0, padx=10)

    close_button = tk.Button(btn_frame, text="Close", width=15, command=this_window.destroy)
    close_button.grid(row=0, column=1, padx=10)
