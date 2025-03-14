import tkinter as tk
from tkinter import ttk

#ftiaximo para8rou
class Extra(tk.Toplevel):
	def __init__(self):
		super().__init__()
		self.title('extra window')
		self.geometry('300x400')
		ttk.Label(self, text = 'A label').pack()
		ttk.Button(self, text = 'A button').pack()
		ttk.Label(self, text = 'another label').pack(expand = True)
            

def create_window_search():
	global extra_window
	extra_window = Extra()

def create_window_save():
	global extra_window
	extra_window = Extra()

def create_window_modify():
	global extra_window
	extra_window = Extra()
      
def create_window_execute():
	global extra_window
	extra_window = Extra()
	

root = tk.Tk()
# root = tk()
root.title("New")
frm = ttk.Frame(root, padding=30)
frm.grid()

#buttons

ttk.Label(frm, text="Search Recipes").grid(column=0, row=0)
ttk.Button(frm, text="Search",command = create_window_search).grid(column=1, row=0)
# .pack(expand = True)



ttk.Label(frm, text="Save Recipe").grid(column=0, row=1)
ttk.Button(frm, text="Save",command = create_window_search).grid(column=1, row=1)

ttk.Label(frm, text="Modify Recipe").grid(column=0, row=2)
ttk.Button(frm, text="Modify",command = create_window_search).grid(column=1, row=2)

ttk.Label(frm, text="Execute Recipe").grid(column=0, row=3)
ttk.Button(frm, text="Execute",command = create_window_search).grid(column=1, row=3)

ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=4)



root.mainloop()





# Dokimastikh klash "Recipe"

class Recipe:
    def __init__(self, name, category, difficulty, time, ingredients, steps):
        self.name = name
        self.category = category
        self.difficulty = difficulty
        self.time = time
        self.ingredients = ingredients
        self.steps = steps


def filter_by_category(recipes, category):
    filtered = []
    for i in recipes:
        if i.category == category:
            filtered.append(i)
    return filtered

recipes = []

gemista = Recipe(name="Μακαρόνια με κιμά", category="Ζυμαρικά", difficulty="", time="", ingredients="", steps="")