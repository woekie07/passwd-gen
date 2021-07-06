from tkinter import *
from random import randint

window = Tk()
window.title("PassWord Gen")
window.geometry("500x300")

def new_rand():
	pw_entry.delete(0, END)

	pw_length = int(me_entry.get())

	my_password = ''

	for x in range(pw_length):
		my_password += chr(randint(33,126))

	pw_entry.insert(0, my_password)

def clip():
    
	window.clipboard_clear()
	
	window.clipboard_append(pw_entry.get())


lf = LabelFrame(window, text="select character between 8 and 12")
lf.pack(pady=20)

me_entry = Entry(lf, font=("Helvetica", 24))
me_entry.pack(pady=20, padx=20)

pw_entry = Entry(window, text='', font=("Helvetica", 24))
pw_entry.pack(pady=20)

f = Frame(window)
f.pack(pady=20)

b = Button(f, text="Generate A Strong Password!", command=new_rand)
b.grid(row=0, column=0, padx=10)

c_button = Button(f, text="Copy To Clipboard", command=clip)
c_button.grid(row=0, column=1, padx=10)

window.mainloop()

