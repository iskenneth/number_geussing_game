import tkinter as tk

root = tk.Tk()
root.title("My First Tkinter Window")

label = tk.Label(root, text="Hello, Tkinter!")
label.pack()

root.mainloop()
