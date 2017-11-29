from tkinter import Tk, messagebox, simpledialog, filedialog

# hide main window
root = Tk()
root.withdraw()
root.update()

result = messagebox.showinfo('Info', 'For your information only')
print(result)

result = messagebox.askyesno('Yes or no', 'What is your answer?')
print(result)

result = simpledialog.askstring("Password","What's the password?")
print(result)

result = simpledialog.askinteger('Ask age','How old are you?')
print(result)

result = simpledialog.askfloat('GPA','What is your GPA?')
print(result)

result = filedialog.askopenfilename()
print(result)

result = filedialog.asksaveasfilename()
print(result)
