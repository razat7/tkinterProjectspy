import tkinter as tk

root = tk.Tk()
root.title("Rate Of Interest")

def compound_interest():
    investment = int(entry1.get())
    income = int(entry2.get())
    profit = income - investment
    roi = profit/investment*100
    profit_label.config(text=profit)
    roi_label.config(text=roi)


label1 = tk.Label(root, text="Investment : ")
label1.grid(row=1, column=1, pady=10, padx=30)

entry1 = tk.Entry(root, text= "")
entry1.grid(row=1, column=2, pady=10, padx=30)


label2 = tk.Label(root, text="Income : ")
label2.grid(row=4, column=1, pady=10, padx=30)

entry2 = tk.Entry(root, text= "")
entry2.grid(row=4, column=2, pady=10, padx=30)

label3 = tk.Label(root, text="PROFIT : ")
label3.grid(row=6, column=1,pady=10, padx=30)

profit_label = tk.Label(root, text=" ")
profit_label.grid(row=6, column=2,pady=10, padx=30)

label4 = tk.Label(root, text="ROI : ")
label4.grid(row=7, column=1,pady=10, padx=30)

roi_label = tk.Label(root, text=" ")
roi_label.grid(row=7, column=2,pady=10, padx=30)

button = tk.Button(root, text="Calc", command=compound_interest)
button.grid(row=10, column=2,pady=10, padx=30)



root.mainloop()
