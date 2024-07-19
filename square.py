import tkinter as tk 
from tkinter import messagebox

root = tk.Tk()
root.title("Square Finder")
root.geometry("700x500")

def square():
    value = int(t_entry.get())
    square_val = value*value
    messagebox.showinfo("Out Put", f"{square_val}")


t_entry= tk.Entry(root, text="Enter Num: ")
t_entry.pack()

button = tk.Button(root, text ="Root", command = square)
button.pack()


root.mainloop()