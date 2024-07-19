import tkinter as tk
from tkinter import messagebox
import csv

root = tk.Tk()
root.title("Bank Records")
root.geometry("700x500")

def adddata():      
        value1= entry1.get()
        value2 = entry2.get()
        f = open("customer.csv","a")
        f.write(f"{value1}, {value2}\n")
        messagebox.showinfo("Success", "Data added successfully!")

def viewdata():
    listdata = []
    with open("customer.csv", 'r') as file:
       datalist = csv.reader(file)
       for row in datalist:      
         listdata.append(row)
    return(listdata)
       
def getdata():
    listsdata = viewdata()
    data_str = "\n".join([", ".join(row) for row in listsdata])
    # messagebox.showinfo("User Details", f"Your Name is {value1} and your address is {value2}")
    label3.config(text=f"{data_str}")


#for label one
label1 = tk.Label(root, text="Enter Name : ")
label1.pack(pady=5)

entry1 = tk.Entry(root, text="")
entry1.pack(pady=5)

#forl label2 
label2 = tk.Label(root, text="Enter Address : ")
label2.pack(pady=5)

entry2 = tk.Entry(root, text="")
entry2.pack(pady=5)

#data submit button
button = tk.Button(root, text="Export to CSV", command=adddata)
button.pack(pady=5)

#data view button
viewbutton = tk.Button(root, text="View Data", command=getdata)
viewbutton.pack(pady=5)

#display data
label3 = tk.Label(root, text="", fg="white", bg="orange",padx=30, pady=50)
label3.pack(pady=5)

root.mainloop()

