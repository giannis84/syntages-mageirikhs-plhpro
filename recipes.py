import tkinter as tk
from tkinter import ttk

# Test data for development and a class for the recipes
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

Spaghetti_meatballs = Recipe(name="Μακαρόνια με κιμά", category="Ζυμαρικά", difficulty="", time="", ingredients="", steps="")


# Main Function
def main():
	#ftiaximo para8rou
	class Search(tk.Toplevel):
		def __init__(self):
			super().__init__()
			self.title('Search')
			self.geometry('300x400')
			ttk.Label(self, text = 'A label').pack()
			ttk.Button(self, text = '1').pack()
			ttk.Label(self, text = 'another label').pack(expand = True)


	# class Submit(tk.Toplevel):
	# 	def __init__(self):
	# 		super().__init__()
	# 		self.title('Submit')
	# 		# self.geometry('300x400')
	# 		self.columnconfigure(0)
	# 		self.columnconfigure(1)
	# 		ttk.Label(self, text = 'A label').pack()
	# 		ttk.Button(self, text = '2').pack()
	# 		# ttk.Label(self, text = f'{Spaghetti_meatballs.name}').pack(expand = True)
	# 		ttk.Label(self, text='Name of the recipe').pack()
	# 		ttk.Entry().grid(column=1, row=3)

	class Modify(tk.Toplevel):
		def __init__(self):
			super().__init__()
			self.title('Modify')
			self.geometry('300x400')
			ttk.Label(self, text = 'A label').pack()
			ttk.Button(self, text = '3').pack()
			ttk.Label(self, text = 'another label').pack(expand = True)

	class Execute(tk.Toplevel):
		def __init__(self):
			super().__init__()
			self.title('Execute')
			self.geometry('300x400')
			ttk.Label(self, text = 'A label').pack()
			ttk.Button(self, text = '4').pack()
			ttk.Label(self, text = 'another label').pack(expand = True)


	def create_window_Search():
		global extra_window
		extra_window = Search()

	# def create_window_Submit():
	# 	global extra_window
	# 	extra_window = Submit()

	def create_window_modify():
		global extra_window
		extra_window = Modify()
		
	def create_window_execute():
		global extra_window
		extra_window = Execute()
		

	root = tk.Tk()
	root.title("Recipes")
	frm = ttk.Frame(root, padding=30)
	frm.grid()

	#buttons

	ttk.Label(frm, text="Search Recipes").grid(column=0, row=0)
	ttk.Button(frm, text="Search",command = create_window_Search).grid(column=1, row=0)
	# .pack(expand = True)



	# Δευτερεύοντα παράθυρα

	def window_submit():

		def save_text():
			user_input = entry.get()  # Get the text from entry
			print(f"Saving recipe: {user_input}")

		new_window = tk.Toplevel(root)
		new_window.title("Submit Recipe")
		new_window.geometry("300x150")
		
		label = tk.Label(new_window, text="Name:")
		label.pack(pady=5)
		
		entry = tk.Entry(new_window)
		entry.pack(pady=5)

		save_button = tk.Button(new_window, text="Save", command=save_text)
		save_button.pack(pady=5)
		
		close_button = tk.Button(new_window, text="Close", command=new_window.destroy)
		close_button.pack(pady=5)


	# Κύριο παράθυρο

	ttk.Label(frm, text="Submit Recipe").grid(column=0, row=1)
	ttk.Button(frm, text="Submit",command = window_submit).grid(column=1, row=1)

	ttk.Label(frm, text="Modify Recipe").grid(column=0, row=2)
	ttk.Button(frm, text="Modify",command = create_window_modify).grid(column=1, row=2)

	ttk.Label(frm, text="Execute Recipe").grid(column=0, row=3)
	ttk.Button(frm, text="Execute",command = create_window_execute).grid(column=1, row=3)

	ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=4)



	root.mainloop()

if __name__ == "__main__":
	main()