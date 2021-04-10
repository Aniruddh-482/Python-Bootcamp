# Tkinter Layout Managers #
# ----------------------- #

# > Pack():  # pack():  The Pack geometry manager packs widgets in rows or columns.
# Put a widget inside a frame (or any other container widget), and have it fill the entire frame. 
# Place a number of widgets on top of each other. Place a number of widgets side by side.

# > Place(): # place(): The Place geometry manager is the simplest of the three general geometry managers provided in Tkinter.
# It allows you explicitly set the position and size of a window, either in absolute terms, or relative to another window.
# To put a particular widget to a precise position

# > Grid():  # grid(): The Grid geometry manager puts the widgets in a 2-dimensional table.
# The master widget is split into a number of rows and columns, and each “cell” in the resulting table can hold a widget. 
# The grid manager is the most flexible of the geometry managers in Tkinter.

# WARNING: we can't mix up grid() and pack() in the same program.
# We can't use grid() and pack() both in the same programe.
# It gives Error

# Padding: Add space around window or any specific widget so that they are not all crushed together.

# For Example:

from tkinter import *

def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)  # Padding around whole window

# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
# my_label.pack()
# my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)  # Padding around specific widget(label)

# Button
button = Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

# Entry
input = Entry(width=10)
print(input.get())
# input.pack()
input.grid(column=3, row=2)

window.mainloop()
