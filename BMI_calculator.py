from tkinter import *
import customtkinter

root = customtkinter.CTk()
root.title("Body Mass Index Calculator")
root.geometry("400x300")  
root.resizable(False, False)

def calculate():
    weight = float(entry_weight.get())
    height = float(entry_height.get())
    bmi = round(((weight / (height ** 2)) * 10000), 1)
    status = ""
    if bmi > 0:
        if bmi < 18.5:
            status = "Underweight"
        elif bmi <= 24:
            status = "Normal"
        elif bmi <= 29.9:
            status = "Overweight"
    label_result.configure(text=f"Your BMI is: {bmi}, {status}")

def clear():
    entry_weight.delete(0, 'end')
    entry_height.delete(0, 'end')
    label_result.configure(text="")

label_weight = customtkinter.CTkLabel(root, text="Weight (kg):", text_color="#D9D9D9", font=("Arial", 19, "bold"), fg_color="#333840")
label_weight.grid(column=0, row=0, padx=10, pady=10, sticky=W)

entry_weight = customtkinter.CTkEntry(root, width=200, corner_radius=5)
entry_weight.grid(column=1, row=0, padx=10, pady=10)

label_height = customtkinter.CTkLabel(root, text="Height (cm):", text_color="#D9D9D9", font=("Arial", 19, "bold"), fg_color="#333840")
label_height.grid(column=0, row=1, padx=10, pady=10, sticky=W)

entry_height = customtkinter.CTkEntry(root, width=200, corner_radius=5)
entry_height.grid(column=1, row=1, padx=10, pady=10)

label_result = customtkinter.CTkLabel(root, text="", text_color="#D9D9D9", font=("Arial", 22, "bold"), fg_color="#333840")
label_result.grid(column=0, columnspan=2, row=3)  

calc_btn = customtkinter.CTkButton(root, text="Calculate", command=calculate, font=("Arial", 22, "bold"), text_color="#D9D9D9", fg_color="#4A6FA5", width=120, height=55, corner_radius=5)
calc_btn.grid(column=0, row=2, padx=10, pady=20)

reset_btn = customtkinter.CTkButton(root, text="Reset", command=clear, font=("Arial", 22, "bold"), text_color="#D9D9D9", fg_color="#4A6FA5", width=120, height=55, corner_radius=5)
reset_btn.grid(column=1, row=2, padx=10, pady=20)

root.mainloop()
