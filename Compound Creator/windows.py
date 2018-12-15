import tkinter as tk

root = tk.Tk()
root.geometry("100x100")


def open():
    top = Toplevel()


open = tk.Button(root, text="Open Window", command=open)
open.config(width=10, height=2)
open.pack()


root.mainloop()
