from tkinter import *
import tkinter as tk
from tkinter import ttk
import window_submit, window_search


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

	# Κύριο παράθυρο

	ttk.Label(frm, text="Submit Recipe").grid(column=0, row=1)
	ttk.Button(frm, text="Submit",command = lambda: window_submit.create_window_submit(root)).grid(column=1, row=1)

	ttk.Label(frm, text="Search Recipe").grid(column=0, row=2)
	ttk.Button(frm, text="Search",command = lambda: window_search.create_window_search(root)).grid(column=1, row=2)

	# ttk.Label(frm, text="Modify Recipe").grid(column=0, row=2)
	# ttk.Button(frm, text="Modify",command = create_window_modify).grid(column=1, row=2)

	ttk.Label(frm, text="Execute Recipe").grid(column=0, row=3)
	ttk.Button(frm, text="Execute",command = create_window_execute).grid(column=1, row=3)

	ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=4)



	root.mainloop()

if __name__ == "__main__":
	main()