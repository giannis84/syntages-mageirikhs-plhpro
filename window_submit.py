from tkinter import *
import tkinter as tk
from tkinter import ttk
import handle_data

def create_window_submit(parent):
        '''Συνάρτηση ορισμού του παραθύρου "Submit recipe"'''
        
        def save_text():
            '''Εντολή αποθήκευσης σε αντικείμενο της κλάσης Recipe'''
            names = entry1.get()
            categories = entry2.get()
            difficulties = entry3.get()
            new_recipe = handle_data.Recipe(name=names, category=categories, difficulty=difficulties)
            handle_data.recipes.append(new_recipe)
            handle_data.save_recipe_to_db(new_recipe)
            print(f"Saved new recipe: {new_recipe.name} in category: {new_recipe.category}, difficulty: {new_recipe.difficulty} and id: {new_recipe.id}. Number of recipes: {len(handle_data.recipes)}")
            handle_data.show_all_recipes()

        this_window = tk.Toplevel(parent) # Κατασκευή Toplevel widget που έχει ως parent το root widget (κυρίως παράθυρο)
        this_window.title("Submit recipe details")
        this_window.geometry("400x200")
        
        frame1 = tk.Frame(this_window)
        frame1.pack(pady=5)
        label1 = tk.Label(frame1, text="Recipe name:")
        label1.pack(side=tk.LEFT, padx=8)
        entry1 = tk.Entry(frame1)
        entry1.pack(side=tk.RIGHT)
        
        frame2 = tk.Frame(this_window)
        frame2.pack(pady=5)
        label2 = tk.Label(frame2, text="Category:")
        label2.pack(side=tk.LEFT, padx=20)
        entry2 = tk.Entry(frame2)
        entry2.pack(side=tk.RIGHT)
        
        difficulty_options = ["Easy", "Medium", "Hard"]
        frame3 = tk.Frame(this_window)
        frame3.pack(pady=5)
        label3 = tk.Label(frame3, text="Difficulty:")
        label3.pack(side=tk.LEFT, padx=20)
        entry3 = ttk.Combobox(frame3, values=difficulty_options)
        entry3.pack(side=tk.RIGHT)
        
        save_button = tk.Button(this_window, text="Save", command=save_text)
        save_button.pack(pady=15)
        
        close_button = tk.Button(this_window, text="Close", command=this_window.destroy)
        close_button.pack(pady=0)