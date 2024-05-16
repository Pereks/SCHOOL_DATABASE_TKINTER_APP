from tkinter import *
import backend2copy

backend2copy.connect()

def read_all_and_refresh():
    read_all()
    listbox.selection_clear(0, END)

def create_entry_and_refresh():
    create_entry()
    read_all_and_refresh()

def update_course_and_refresh():
    update_course()
    read_all_and_refresh()

def delete_course_and_refresh():
    delete_course()
    read_all_and_refresh()

def get_selected_row(event):
    global selected_row
    index = listbox.curselection()
    if index:
        selected_row = listbox.get(index[0])

root = Tk()
root.title("Online School")
root.geometry("1000x500")           

name = Label(root, text="Course Name", padx=10, pady=20, font=("Helvetica", 20))
name.grid(row=0, column=0)

name_text = StringVar()
name_entry = Entry(root, textvariable=name_text)
name_entry.grid(row=0, column=1)

category = Label(root, text="Category", padx=10, pady=20, font=("Helvetica", 20))
category.grid(row=1, column=0)

category_text = StringVar()
category_entry = Entry(root, textvariable=category_text)
category_entry.grid(row=1, column=1)

author = Label(root, text="Author", padx=10, pady=20, font=("Helvetica", 20))
author.grid(row=0, column=2)

author_text = StringVar()
author_entry = Entry(root, textvariable=author_text)
author_entry.grid(row=0, column=3)

price = Label(root, text="Price", padx=10, pady=20, font=("Helvetica", 20))
price.grid(row=1, column=2)

price_text = StringVar()
price_entry = Entry(root, textvariable=price_text)
price_entry.grid(row=1, column=3)

listbox = Listbox(root, height=10, width=60)
listbox.grid(row=2, column=0, rowspan=4, columnspan=2)
listbox.bind("<<ListboxSelect>>", get_selected_row)

def create_entry():
    backend2copy.create(name_text.get(), category_text.get(), author_text.get(), price_text.get())
    read_all_and_refresh()

create_entry_button = Button(root, text="Create Course", font=("Helvetica", 30), command=create_entry_and_refresh)
create_entry_button.grid(row=4, column=3)

def read_all():
    listbox.delete(0, END)
    rows = backend2copy.read_all()
    for idx, row in enumerate(rows, start=1):  # Start counting from 1
        listbox.insert(END, (idx,) + row[1:])  # Insert row number as the first element

read_all_button = Button(root, text="Show All Courses", font=("Helvetica", 30), command=read_all_and_refresh)
read_all_button.grid(row=5, column=3)

def update_course():
    if listbox.curselection():
        selected_row = listbox.curselection()[0]  # Get the index of the selected row
        selected_id = selected_row + 1  # Convert index to row number (index starts from 0)
        selected_data = listbox.get(selected_row)  # Get the data of the selected row
        backend2copy.update(selected_id, selected_data[1], selected_data[2], selected_data[3], selected_data[4])
        read_all_and_refresh()

update_button = Button(root, text="Update Course", font=("Helvetica", 30), command=update_course_and_refresh)
update_button.grid(row=6, column=3)

def delete_course():
    if listbox.curselection():
        selected_row = listbox.curselection()[0]  # Get the index of the selected row
        selected_id = selected_row + 1  # Convert index to row number (index starts from 0)
        backend2copy.delete_course(selected_id)
        read_all_and_refresh()

delete_button = Button(root, text="Delete Course", font=("Helvetica", 30), command=delete_course_and_refresh)
delete_button.grid(row=7, column=3)

listbox.bind("<<ListboxSelect>>", get_selected_row)

read_all_and_refresh()

root.mainloop()
