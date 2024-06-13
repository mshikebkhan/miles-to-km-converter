from tkinter import *

def calculate():
    kms = float(input.get()) * 1.609
    kms = round(kms)
    output.config(text=kms)

# Window Setup
window = Tk()
window.title("Mile to KM Converter")
window.minsize(width=330, height=180)
window.config(padx=20, pady=20)

# Input
input = Entry(width=10)
input.grid(column=1, row=0)

# Input Label
input_label = Label(text="Miles", font=("Arial", 16, "bold"))
input_label.grid(column=2, row=0)

# Output Label
output_label = Label(text="is equal to", font=("Arial", 16, "bold"))
output_label.grid(column=0, row=2)

# Output
output = Label(text="0", font=("Arial", 16, "bold"))
output.grid(column=1, row=2)

# Output Label 2
output_label_2 = Label(text="KM", font=("Arial", 16, "bold"))
output_label_2.grid(column=2, row=2)

# Calculate Button
calculate_button = Button(text="Calculate", font=("Arial", 16, "bold"), command=calculate)
calculate_button.grid(column=1, row=3)

window.mainloop()

