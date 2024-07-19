import tkinter as tk 
from tkinter import messagebox

root = tk.Tk()
root.title("Simple Interest")
root.geometry("700x500")

def simpleInterest():
    value1 =float(p_value.get())
    value2 = float(t_value.get())
    value3 =float(r_value.get())
    total =value1*value2*value3/100
    messagebox.showinfo("Out Put", f"{total}")


p_label = tk.Label(root, text="Enter value for P : ")
p_label.pack(pady=5)
p_value = tk.Entry(root, text="")
p_value.pack(pady=5)

t_label = tk.Label(root, text="Enter value for T : ")
t_label.pack(pady=5)
t_value = tk.Entry(root, text="")
t_value.pack(pady=5)

r_label = tk.Label(root, text="Enter value for R : ")
r_label.pack(pady=5)
r_value = tk.Entry(root, text="")
r_value.pack(pady=5)

button = tk.Button(root, text = "Calculate",command=simpleInterest)
button.pack()



root.mainloop()

