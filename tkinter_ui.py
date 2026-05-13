from tkinter import *
from tkinter import messagebox
from pathlib import Path
import os

root = Tk()
root.title("CRUD File Management System")
root.geometry("500x500")


# ---------- FUNCTIONS ----------

def create_file():
    file_name = entry_file.get()
    content = text_area.get("1.0", END)

    p = Path(file_name)

    if p.exists():
        messagebox.showerror("Error", "File already exists")

    else:
        with open(file_name, 'w') as file:
            file.write(content)

        messagebox.showinfo("Success", "File created successfully")



def read_file():
    file_name = entry_file.get()

    p = Path(file_name)

    if p.exists():
        with open(file_name, 'r') as file:
            content = file.read()

        text_area.delete("1.0", END)
        text_area.insert(END, content)

    else:
        messagebox.showerror("Error", "File does not exist")



def update_file():
    file_name = entry_file.get()
    content = text_area.get("1.0", END)

    p = Path(file_name)

    if p.exists():
        with open(file_name, 'w') as file:
            file.write(content)

        messagebox.showinfo("Success", "File updated successfully")

    else:
        messagebox.showerror("Error", "File does not exist")



def delete_file():
    file_name = entry_file.get()

    p = Path(file_name)

    if p.exists():
        os.remove(file_name)

        messagebox.showinfo("Success", "File deleted successfully")

    else:
        messagebox.showerror("Error", "File does not exist")


# ---------- UI ----------

label_title = Label(root, text="CRUD File Management System", font=("Arial", 18, "bold"))
label_title.pack(pady=10)

label_file = Label(root, text="Enter File Name")
label_file.pack()

entry_file = Entry(root, width=40)
entry_file.pack(pady=5)

text_area = Text(root, width=50, height=15)
text_area.pack(pady=10)

btn_create = Button(root, text="Create", width=15, command=create_file)
btn_create.pack(pady=5)

btn_read = Button(root, text="Read", width=15, command=read_file)
btn_read.pack(pady=5)

btn_update = Button(root, text="Update", width=15, command=update_file)
btn_update.pack(pady=5)

btn_delete = Button(root, text="Delete", width=15, command=delete_file)
btn_delete.pack(pady=5)

root.mainloop()

