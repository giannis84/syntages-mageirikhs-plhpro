from tkinter import *


main_window = Tk()
main_window.title('Submit')

main_window.columnconfigure(0, weight=1)
main_window.columnconfigure(1, weight=1)
main_window.geometry('600x400')

name_label = Label(main_window, text="Ονομα:")
name_label.grid(column=0, row=1)
name_label_field_name = Entry()
name_label_field_name.grid(column=1, row=1)


name_label = Label(main_window, text="Κατηγορία:")
name_label.grid(column=0, row=2)
name_label_field = Entry()
name_label_field.grid(column=1, row=2)


name_label = Label(main_window, text="Δυσκολία:")
name_label.grid(column=0, row=3)
name_label_field = Entry()
name_label_field.grid(column=1, row=3)


name_label = Label(main_window, text="Χρονος:")
name_label.grid(column=0, row=4)
name_label_field = Entry()
name_label_field.grid(column=1, row=4)

name_label = Label(main_window, text="Υλικά:")
name_label.grid(column=0, row=5)
name_label_field = Entry()
name_label_field.grid(column=1, row=5)

name_label = Label(main_window, text="Βηματα:")
name_label.grid(column=0, row=6)
name_label_field = Entry()
name_label_field.grid(column=1, row=6)


main_window.mainloop()