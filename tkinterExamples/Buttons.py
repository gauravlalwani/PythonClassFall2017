from tkinter import Tk,Button,Label

# Response function when the button A is pressed
def responseA():
    y = Label(root, text='You chose A')
    y.pack()

# Response function when the button B is pressed
def responseB():
    y = Label(root, text='You chose B')
    y.pack()


root = Tk()
# Displaying the instruction via a Label widget
t = Label(root, text='Pick your opitions:')
t.pack()

# Button A widget
x1 = Button(root, text='Option A', command=responseA)
x1.pack()

# Button B widget
x2 = Button(root, text='Option B', command=responseB)
x2.pack()

root.mainloop()
