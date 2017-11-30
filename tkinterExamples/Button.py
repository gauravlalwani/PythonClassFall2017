from tkinter import Tk,Button,Label

def response():
    y = Label(root, text='You did it!')
    y.pack()

root = Tk()
x = Button(root, text='Click here!', command=response)
x.pack()
root.mainloop()

