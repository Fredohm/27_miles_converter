# Miles converter
from tkinter import *

window = Tk()
window.minsize(width=300, height=120)
window.config(padx=50, pady=10)
window.title("Miles to Km Converter")


def calculate():
    # 1 mile is 1,60934km
    km = round(float(miles_input.get()) * 1.60934)
    km_output_label.config(text=str(km))


miles_label = Label(text="Miles", padx=10)
km_label = Label(text="Km")
is_equal_label = Label(text="is equal to")
miles_input = Entry(width=10)
km_output_label = Label()
calculate_button = Button(text="Calculate", command=calculate)

miles_input.grid(column=2, row=1, pady=10)
miles_label.grid(column=3, row=1)
is_equal_label.grid(column=1, row=2)
km_output_label.grid(column=2, row=2, pady=3)
km_label.grid(column=3, row=2)
calculate_button.grid(column=2, row=3)

window.mainloop()
