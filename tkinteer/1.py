import tkinter as tk
import tkinter.font as tfont
from tkinter import Entry
from tkinter import ttk
# tk


window = tk.Tk()
window.title("My application")
window.minsize(width=400, height=300)

custom_font = tfont.Font(family="Times New Roman", size=15)

label = tk.Label(text="hello world\n\n\nhave a nice day", font=("Times New Roman", 20, "bold"))
label.pack(side="left")
#label.config(font=("courier New",25))
label["text"] = "have a nice day"
label.config(text="my new app")


def function_button():
    input_text = user_input.get()
    label.config(text=input_text)


# taking user entry 
user_input = tk.Entry(width=10, show="*")
user_input.pack()


# button
button = tk.Button(text="click", command=function_button)
button.pack()

quit_button = tk.Button(text="quit", command=window.destroy)
quit_button.pack()
text =tk.Text(height=5,width=25)
text.pack()
text.focus()#for cursor

text.insert("1.0","enter your comment")#default 
#text [state ] =disable if ypu want to enable or disable
window.mainloop()