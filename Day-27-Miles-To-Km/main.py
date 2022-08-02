from tkinter import *

def button_clicked():
    new_text = float(input.get()) * 1.609
    my_label.config(text=new_text)

window = Tk()
window.title("Miles to Km Converter")
#window.minsize(width=300, height=300)
window.config(padx=50, pady=50)

# Label = is equal to
eq_label = Label(text="is equal to", font=("Arial", 24, "bold"))
eq_label.grid(column=0, row=1)
#my_label.config(padx=50, pady=50)


# Entry = miles entry
input = Entry(text=0, width=10)
input.grid(column=1, row=0)

# Label = Miles
mi_label = Label(text="Miles", font=("Arial", 24, "bold"))
mi_label.grid(column=2, row=0)

# Label = conversion
my_label = Label(text="0", font=("Arial", 24, "bold"))
my_label.grid(column=1, row=1)
#my_label.config(padx=50, pady=50)

# Label = Km
km_label = Label(text="Km", font=("Arial", 24, "bold"))
km_label.grid(column=2, row=1)

# Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)



window.mainloop()
