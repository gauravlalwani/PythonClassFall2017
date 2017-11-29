from tkinter import Tk, simpledialog

# first, data entry via keyboard
print('What is your name?')
userName = input()
print('Your name is ' + userName + '.')


# next, with a simple GUI
# first, some preparation
root = Tk()
root.withdraw()
root.update()
guiInput = simpledialog.askstring('Name entry','What is your name?')
print('Your name is ' + guiInput + '.')
