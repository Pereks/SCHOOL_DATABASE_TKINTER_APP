from tkinter import *
import backendCopy

backendCopy.connect()

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
category_text = Entry(root, textvariable=category_text)
category_text.grid(row=1, column=1)

author = Label(root, text="Author", padx=10, pady=20, font=("Helvetica", 20))
author.grid(row=0, column=2)

author_text = StringVar()
author_text = Entry(root, textvariable=author_text)
author_text.grid(row=0, column=3)

price = Label(root, text="Price", padx=10, pady=20, font=("Helvetica", 20))
price.grid(row=1, column=2)

price_text = StringVar()
price_text = Entry(root, textvariable=price_text)
price_text.grid(row=1, column=3)

def get_selected_row(event):
    global selected_row
    index = listbox.curselection()
    if index:
        selected_row = listbox.get(index)
        print(selected_row)

listbox = Listbox(root, height=10, width=60)
listbox.grid(row=2, column=0, rowspan=4, columnspan=2)
listbox.bind("<<ListboxSelect>>", get_selected_row)

def create_entry():
    backendCopy.create(name_text.get(), category_text.get(), author_text.get(), price_text.get())
    listbox.delete(0, END)
    read_all()

create_entry_button = Button(root, text="Create Course", font=("Helvetica", 30),
                             command=create_entry)
create_entry_button.grid(row=4, column=3)

def read_all():
    listbox.delete(0, END)
    courses = backendCopy.read_all()
    for idx, row in enumerate(courses, start=1):
        # Exclude the course ID (the first element) and insert row number
        listbox.insert(END, f"{idx}. {', '.join(row[1:])}")  

read_all()  # Show all courses when GUI is initialized

def update_course():
    selected_index = listbox.curselection()
    print("Selected Index:", selected_index)  # Debug print
    if selected_index:
        course_id = listbox.get(selected_index[0]).split('.')[0]  # Extracting the course ID from the selected row
        print("Course ID:", course_id)  # Debug print
        backendCopy.update(course_id, name_text.get(), category_text.get(), author_text.get(), price_text.get())
        read_all()  # Refresh the list of courses after update

update_button = Button(root, text="Update Course", font=("Helvetica", 30),
                       command=update_course)
update_button.grid(row=6, column=3)

def delete_course():
    selected_indices = listbox.curselection()
    for index in selected_indices:
        course_id = listbox.get(index).split('.')[0]  # Extracting the course ID from the selected row
        backendCopy.delete(course_id)
    read_all()  # Refresh the list of courses after deletion

delete_button = Button(root, text="Delete Course", font=("Helvetica", 30),
                       command=delete_course)
delete_button.grid(row=7, column=3)

root.mainloop()
