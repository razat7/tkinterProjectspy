import tkinter as tk
from tkinter import PhotoImage

root = tk.Tk()
root.title("BMI CALCULATOR")

image_path = "bmi.png "
logo = PhotoImage(file = image_path)
logo = logo.subsample(4)

def bmicalc():
    name = entry1.get()
    height = float(entry2.get())
    actual_height = height/100
    weight = float(entry3.get())
    bmi = weight/(actual_height*actual_height)
    if bmi >= 25 and bmi <=30:
          textoutput.config(text="You are overweight, You need to do some workout. ")
    elif bmi >= 18.5 and bmi <=24.99:
            textoutput.config(text="Enjoy, You are having a healthy lifestyle.")
    elif bmi < 18.5 :
            textoutput.config(text="You need review your workout schedule and diet plan, or You can go for a doctor.")
    elif bmi > 30 :
        textoutput.config(fg="red", text="You are hugely obese person, Maintain your BMI to stay fit & healthy")
    else:
            textoutput.config(text="There's something wrong, Please check Again")
    output.config(text= f"Hello {name} \n Your BMI is {round(bmi, 2)}")

   

label_logo = tk.Label(root, image=logo)
label_logo.grid(row=0, column=0, columnspan=5)

output = tk.Label(root, fg ="green",  text="YOUR BMI DISPLAYS HERE")
output.grid(row=1, columnspan=5, pady=10, padx=10)

textoutput = tk.Label(root, fg="blue", text=" ")
textoutput.grid(row=4, columnspan=5, pady=10, padx=10)

label1 = tk.Label(root, text="Enter your Name : ")
label1.grid(row=2, column=1, pady=10, padx=10)
entry1 = tk.Entry(root, text="")
entry1.grid(row=2, column=2, pady=10, padx=10)

label2 = tk.Label(root, text="Enter your Height (cm) : ")
label2.grid(row=2, column=3, pady=10, padx=10)
entry2 = tk.Entry(root, text="")
entry2.grid(row=2, column=4, pady=10, padx=10)

label3 = tk.Label(root, text="Enter your Weight (Kg) : ")
label3.grid(row=3, column=1, pady=10, padx=10)
entry3 = tk.Entry(root, text="")
entry3.grid(row=3, column=2, pady=10, padx=10)

button = tk.Button(root, bg = "orange", text="Calculate", command=bmicalc)
button.grid(row=3, column=3, pady=10, padx=10)

root.mainloop()