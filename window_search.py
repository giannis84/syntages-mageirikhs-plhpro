from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import handle_data
import definitions as defs
import window_execute

def create_window_search(parent):
        '''Συνάρτηση ορισμού του παραθύρου "Submit recipe"'''

        handle_data.show_all_recipes() # Για debugging
        
        def display_recipe():
            '''Έρευνα και επιστροφή αντικειμένου της κλάσης Recipe'''
            name = entry1.get()
            recipes = handle_data.search_recipe_by_name(name)
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
                tree.insert("", tk.END, values=(recipe.name, recipe.category, recipe.difficulty, recipe.time, recipe.ingredients, recipe.steps))

            tree.pack(expand=True, fill=tk.BOTH)

            # Μήνυμα εάν δεν βρέθηκαν συνταγές
            if not tree.get_children():
                label = tk.Label(window, text="No recipes found.", fg="red")
                label.pack(pady=10)
            # Κουμπιά Modify και Delete
            button_frame = tk.Frame(window)
            button_frame.pack(pady=10)

            # TODO ΝΑ ΓΡΑΨΩ ΟΠΩΣΔΗΠΟΤΕ ΚΩΔΙΚΑ ΝΑ ΕΠΙΣΤΡΕΦΕΙ ΤΟ ID ΤΗΣ ΣΥΝΤΑΓΗΣ, ΜΕ ΒΑΣΗ ΑΥΤΟ ΠΡΕΠΕΙ ΝΑ ΤΙΣ ΣΒΗΝΩ Η' ΝΑ ΚΑΝΩ MODIFY!!!!!

            def get_selected_recipe_name():
                selected = tree.selection()
                if not selected:
                    return None
                values = tree.item(selected[0])["values"]
                name = values[0]
                print(name)
                return name

            def modify_selected():
                name = get_selected_recipe_name()
                if not name:
                    messagebox.showwarning("No selection", "Please select a recipe to modify.")
                    return
                # Να γράψω τον κώδικα για το modify!!!!
                print(f"Modify: {name}")

            def delete_selected():
                name = get_selected_recipe_name()
                if not name:
                    messagebox.showwarning("No selection", "Please select a recipe to delete.")
                    return
                confirm = messagebox.askyesno("Confirm Deletion", f"Delete recipe '{name}'?")
                if confirm:

                    handle_data.delete_recipe_by_id(name) # Σβήσιμο από την βάση δεδομένων
                    tree.delete(tree.selection()[0])  # Σβήσιμο από το treeview
                    messagebox.showinfo("Deleted", f"Recipe '{name}' was deleted.")

            execute_button = tk.Button(button_frame, text="Execute", command=lambda: window_execute.create_window_execute(parent,recipe.steps))
            execute_button.pack(side=tk.LEFT, padx=10)

            modify_button = tk.Button(button_frame, text="Modify", command=modify_selected)
            modify_button.pack(side=tk.LEFT, padx=10)

            delete_button = tk.Button(button_frame, text="Delete", command=delete_selected)
            delete_button.pack(side=tk.RIGHT, padx=10)


        this_window = tk.Toplevel(parent) # Κατασκευή Toplevel widget που έχει ως parent το root widget (κυρίως παράθυρο)
        this_window.title("Search recipes")
        this_window.geometry("400x200")
        
        frame1 = tk.Frame(this_window)
        frame1.pack(pady=5)
        label1 = tk.Label(frame1, text="Recipe name:")
        label1.pack(side=tk.LEFT, padx=20)
        entry1 = tk.Entry(frame1)
        entry1.pack(side=tk.RIGHT)
        
        save_button = tk.Button(this_window, text="Search", command=display_recipe)
        save_button.pack(pady=15)
        
        close_button = tk.Button(this_window, text="Close", command=this_window.destroy)
        close_button.pack(pady=0)