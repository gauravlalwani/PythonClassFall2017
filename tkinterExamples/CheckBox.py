from tkinter import Tk, Checkbutton

def CheckUncheck():
    print('You checked or unchecked the box.')
    
root = Tk()
x = Checkbutton(root, text='Check this box', command=CheckUncheck)
x.pack()
root.mainloop()


