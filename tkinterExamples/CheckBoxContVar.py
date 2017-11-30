from tkinter import Tk, Checkbutton, IntVar, messagebox

root = Tk()

# defining the control variable
checked = IntVar(value=1)

# check box
x = Checkbutton(root, text='Check this box', variable=checked)
x.pack()
root.mainloop()

# preparing another GUI
root = Tk()
root.withdraw()
root.update()

# depending on the value of the check box ...
if checked.get():
    messagebox.showinfo('Message','The box was checked')
else:
    messagebox.showinfo('Message','The box was unchecked')

