from tkinter import Tk, Label, Radiobutton, StringVar

# crating the root object
root = Tk()

# creagint the srting control variable and set its
speed = StringVar(value='Fast')

# creating a label for the instruction
t1 = Label(root, text='Please select the speed \n for your spaceship:')
t1.pack()

# creagint the radio buttons
r1 = Radiobutton(root, text="Normal" ,variable=speed, value="Normal")
r2 = Radiobutton(root, text="Fast" ,variable=speed, value="Fast")
r3 = Radiobutton(root, text="Super fast" ,variable=speed, value="Super fast")
r1.pack()
r2.pack()
r3.pack()

# keep the GUI window open
root.mainloop()

print(speed.get())
