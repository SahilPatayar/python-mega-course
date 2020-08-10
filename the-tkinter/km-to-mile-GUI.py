from tkinter import *

window = Tk()

def km_to_mile():
    to_miles = float(entry_val.get()) / 1.609
    text1.insert(END, to_miles)

button1 = Button(window, text="KM to Mile", command=km_to_mile)

entry_val = StringVar()
entry1 = Entry(window, textvariable=entry_val)
entry1.grid(row=0, column=0)

text1 = Text(window, height=1, width=20)
text1.grid(row=0, column=1)

button1.grid(row=0, column=2)

window.mainloop()