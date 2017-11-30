from tkinter import Tk, Label

root = Tk()

t_first0 = Label(root, text='Row=0, Col=0')
t_first0.grid(row=0, column=0)

t_first1 = Label(root, text='Row=0, Col=1')
t_first1.grid(row=0, column=1)

t_second = Label(root, text='Row=1, label spanning across 3 columns')
t_second.grid(row=1, column=0, columnspan=3)

t_third = Label(root, text='Row=2, Col=1')
t_third.grid(row=2, column=1)

t_fourth = Label(root, text='Row=3, Col=0')
t_fourth.grid(row=3, column=0)

t_fifth = Label(root, text='Row=4, Col=2')
t_fifth.grid(row=4, column=2)

root.mainloop()


