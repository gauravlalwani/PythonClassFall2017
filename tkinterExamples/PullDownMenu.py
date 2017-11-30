from tkinter import Tk, Label, OptionMenu, StringVar

# crating the root object
root = Tk()

# creagint the srting control variable and set its
speed = StringVar(value='Super fast')

# creating a label for the instruction
t1 = Label(root, text='Please select the speed \n for your spaceship:')
t1.pack()

# creagint the radio buttons
r1 = OptionMenu(root, speed, 'Normal', 'Fast', 'Super fast')
r1.pack()

# keep the GUI window open
root.mainloop()

print(speed.get())
