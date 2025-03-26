from tkinter import *
import tkinter as tk
from tkinter import ttk
import handle_data


# Main Function
def main():
	# Πρώτη προσπάθεια να φτιάξουμε κώδικα δημιουργίας παραθύρων
	# Χρησιμοποιήσαμε κλάσεις που κληρονομούν από την κλάση tk.Toplevel
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

	# Συναρτήσεις που δημιουργούν αντικείμενα των κλάσεων των παραθύρων που θέλουμε να δημιουργήσουμε
	# Δεν καλούνται άμεσα αλλά ορίζονται ως δείκτες "command" μέσα σε αντικείμενα του module ttk
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
		

	# Δημιουργία κυρίως παραθύρου
	root = tk.Tk()
	root.title("Recipes")
	frm = ttk.Frame(root, padding=30)
	frm.grid()

	# Δευτερεύοντα παράθυρα μπορούν να δημιουργηθούν απευθείας με συναρτήσεις αντί να ορίζουμε κλάσεις όπως πιο πριν
	def create_window_submit():
			'''Συνάρτηση ορισμού του παραθύρου "Submit recipe"'''
			
			def save_text():
				'''Εντολή αποθήκευσης σε αντικείμενο της κλάσης Recipe'''
				names = entry1.get()
				categories = entry2.get()
				difficulties = entry3.get()
				new_recipe = handle_data.Recipe(name=names, category=categories, difficulty=difficulties)
				handle_data.recipes.append(new_recipe)
				print(f"Saved new recipe: {new_recipe.name} in category: {new_recipe.category}, difficulty: {new_recipe.difficulty} and id: {new_recipe.id}. Number of recipes: {len(handle_data.recipes)}")

			this_window = tk.Toplevel(root) # Κατασκευή Toplevel widget που έχει ως parent το root widget (κυρίως παράθυρο)
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


	# Κύριο παράθυρο

	ttk.Label(frm, text="Submit Recipe").grid(column=0, row=1)
	ttk.Button(frm, text="Submit",command = create_window_submit).grid(column=1, row=1)

	ttk.Label(frm, text="Modify Recipe").grid(column=0, row=2)
	ttk.Button(frm, text="Modify",command = create_window_modify).grid(column=1, row=2)

	ttk.Label(frm, text="Execute Recipe").grid(column=0, row=3)
	ttk.Button(frm, text="Execute",command = create_window_execute).grid(column=1, row=3)

	ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=4)



	root.mainloop()

if __name__ == "__main__":
	main()