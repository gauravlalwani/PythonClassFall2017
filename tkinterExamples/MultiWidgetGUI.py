from tkinter import Tk, Entry, Label, Button, StringVar
from PigLatin import PigLatin

# pig latin translation wrapper
def PigLatinWrapper():
    inString = EngWord.get()
    PLWord = PigLatin(inString)
    OutWord.set(PLWord)


root = Tk()

EngWord = StringVar()
OutWord = StringVar()

t1 = Label(root, text="English to Pig Latin translator")
t1.grid(row=0, column=0, columnspan=2)

t2 = Label(root, text="English:")
t2.grid(row=1, column=0)

e1 = Entry(root, textvariable=EngWord)
e1.grid(row=1, column=1)

t3 = Label(root, text='Pig Latin:')
t3.grid(row=2, column=0)

t4 = Label(root, textvariable=OutWord)
t4.grid(row=2, column=1)

b1 = Button(root, text='Translate', command=PigLatinWrapper)
b1.grid(row=3, column=1)

root.mainloop()
