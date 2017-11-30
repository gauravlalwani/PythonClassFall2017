from tkinter import Tk,Entry, StringVar, Label

root = Tk()

# text control variable
sValue = StringVar()

t1 = Label(root, text='Type in some text here!')
t1.pack()

x = Entry(root, textvariable=sValue)
x.pack()

root.mainloop()
print(sValue.get())


