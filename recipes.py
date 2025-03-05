from tkinter import *
from tkinter import ttk

root = Tk()
root.title("New")
frm = ttk.Frame(root, padding=30)
frm.grid()

ttk.Label(frm, text="Search Recipes").grid(column=0, row=0)
ttk.Button(frm, text="Search").grid(column=1, row=0)

ttk.Label(frm, text="Save Recipe").grid(column=0, row=1)
ttk.Button(frm, text="Save").grid(column=1, row=1)

ttk.Label(frm, text="Modify Recipe").grid(column=0, row=2)
ttk.Button(frm, text="Modify").grid(column=1, row=2)

ttk.Label(frm, text="Execute Recipe").grid(column=0, row=3)
ttk.Button(frm, text="Execute").grid(column=1, row=3)

ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=4)

root.mainloop()