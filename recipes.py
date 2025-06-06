from tkinter import *
import tkinter as tk
from tkinter import ttk
import window_submit, window_search

# Main Function
def main():	
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

	ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=4)

	root.mainloop()

if __name__ == "__main__":
	main()