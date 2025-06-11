from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import json
import handle_data
import window_execute, window_submit

def create_window_search(parent):
        '''Συνάρτηση ορισμού του παραθύρου "Submit recipe"'''

        handle_data.show_all_recipes() # Για debugging
        
        def display_recipe():
            '''Έρευνα και επιστροφή αντικειμένου της κλάσης Recipe'''
            name = entry1.get()
            category = entry2.get()
            recipes = handle_data.search_recipe_by_name_or_cat(name,category)
            display_recipe_list_window(recipes)

        def display_recipe_list_window(recipes):
            '''Δημιουργεί νέο παράθυρο και εμφανίζει τις συνταγές σε μορφή πίνακα'''

            window = tk.Toplevel()
            window.title("Search Results")
            window.geometry("800x300")

            tree = ttk.Treeview(window, columns=("Name", "Category", "Difficulty", "Time", "Ingredients", "Steps"), show="headings")

            tree.heading("Name", text="Name")
            tree.heading("Category", text="Category")
            tree.heading("Difficulty", text="Difficulty")
            tree.heading("Time", text="Time")
            tree.heading("Ingredients", text="Ingredients")
            tree.heading("Steps", text="Steps")

            tree.column("Name", width=150)
            tree.column("Category", width=100)
            tree.column("Difficulty", width=80)
            tree.column("Time", width=80)
            tree.column("Ingredients", width=200)
            tree.column("Steps", width=200)

            # Populate rows
            for recipe in recipes:
                # Προσπέρνα τις "άδειες" συνταγές
                if all(not getattr(recipe, attr) for attr in ["name", "category", "difficulty", "time", "ingredients", "steps"]):
                    continue

                # nice ingredients text!
                ingredients_text = ""
                if recipe.ingredients != "":
                    recipe_ingredients_list = json.loads(recipe.ingredients)
                    for i, ingredient in enumerate(recipe_ingredients_list):
                        ingredients_text += ingredient['name']
                        if i != len(recipe_ingredients_list) - 1:
                            ingredients_text += ", "

                # nice steps text and total time!
                steps_text = ""
                time_text = ""
                total_time = 0
                if recipe.steps != "":
                    list_of_steps = json.loads(recipe.steps)
                    steps_text = f"{len(list_of_steps)} execution steps"
                    for step in list_of_steps:
                        total_time += int(step['time'])
                if total_time != 0:
                    time_text = str(total_time)

                # Edw ginetai to display!!
                tree.insert("", tk.END, values=(recipe.name, recipe.category, recipe.difficulty, time_text, ingredients_text, steps_text))

            tree.pack(expand=True, fill=tk.BOTH)

            # Μήνυμα εάν δεν βρέθηκαν συνταγές
            if not tree.get_children():
                label = tk.Label(window, text="No recipes found.", fg="red")
                label.pack(pady=10)
            # Κουμπιά Modify και Delete
            button_frame = tk.Frame(window)
            button_frame.pack(pady=10)

            def get_selected_recipe_name():
                selected = tree.selection()
                if not selected:
                    return None
                values = tree.item(selected[0])["values"]
                name = values[0]
                return name
            
            def get_selected_recipe():
                selected = tree.selection()
                if not selected:
                    return None
                index = tree.index(selected[0])
                return recipes[index]

            def modify_selected():
                recipe_to_modify = get_selected_recipe()
                if not recipe_to_modify:
                    messagebox.showwarning("No selection", "Please select a recipe to modify.")
                    return
                print(f"Modify: {get_selected_recipe_name()}")
                window_submit.create_window_submit(parent, get_selected_recipe())


            def delete_selected():
                name = get_selected_recipe_name()
                if not name:
                    messagebox.showwarning("No selection", "Please select a recipe to delete.")
                    return
                confirm = messagebox.askyesno("Confirm Deletion", f"Delete recipe '{name}'?")
                if confirm:
                    recipe_to_delete = get_selected_recipe()
                    handle_data.delete_recipe_by_id(recipe_to_delete.id) # Σβήσιμο από την βάση δεδομένων
                    tree.delete(tree.selection()[0])  # Σβήσιμο από το treeview
                    messagebox.showinfo("Deleted", f"Recipe '{name}' was deleted.")

            
            execute_button = tk.Button(button_frame, text="Execute", command=lambda: window_execute.create_window_execute(parent,get_selected_recipe().steps,get_selected_recipe().ingredients))
            execute_button.pack(side=tk.LEFT, padx=10)

            modify_button = tk.Button(button_frame, text="Modify", command=modify_selected)
            modify_button.pack(side=tk.LEFT, padx=10)

            close_button = tk.Button(button_frame, text="Close", command=window.destroy)
            close_button.pack(side=tk.RIGHT, padx=10)

            delete_button = tk.Button(button_frame, text="Delete", command=delete_selected)
            delete_button.pack(side=tk.RIGHT, padx=10)


        this_window = tk.Toplevel(parent) # Κατασκευή Toplevel widget που έχει ως parent το root widget (κυρίως παράθυρο)
        this_window.title("Search recipes")
        this_window.geometry("400x200")
        frame1 = ttk.Frame(this_window )
        frame1.grid(row=0, column=0,sticky="ew",padx=100)
        # ,pady=200
        ttk.Label(frame1, text="Ονομα:").grid(row=0, column=0,sticky="ew")
        
        entry1 = ttk.Entry(frame1)
        entry1.grid(row=0, column=1,sticky="ew")

        ttk.Label(frame1, text="Κατηγορια:").grid(row=1, column=0)

        entry2 = ttk.Entry(frame1)
        entry2.grid(row=1, column=1,sticky="ew")
    
        add_button = ttk.Button(frame1, text="Αναζήτηση Συνταγής", command=display_recipe)
        add_button.grid(row=2, column=0, columnspan=2 ,sticky="ew")

        close_button = tk.Button(frame1, text="Close", command=this_window.destroy)
        close_button.grid(row=3, column=0, columnspan=2 ,sticky="ew")

        
