import tkinter as tk
import tkinter.font as tfont

window = tk.Tk()
window.title("My Application")
window.minsize(width=400, height=300)

custom_font = tfont.Font(family="Times New Roman", size=20, weight="bold")

# Main label
label = tk.Label(window, text="My new app", font=custom_font)
label.pack(pady=(20, 10))

# Entry widget
user_input = tk.Entry(window, width=25, font=("Times New Roman", 15))
user_input.pack(pady=5)

# Button function
def function_button():
	input_text = user_input.get()
	label.config(text=input_text)

# Click button
button = tk.Button(window, text="Click", command=function_button, width=15)
button.pack(pady=5)

# Quit button
quit_button = tk.Button(window, text="Quit", command=window.destroy, width=15)
quit_button.pack(pady=5)

window.mainloop()
