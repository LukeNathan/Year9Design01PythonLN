import tkinter as tk
import random

root = tk.Tk()
root.geometry("500x1000")

form = tk.Label(root, text="Formula")
form.grid(row=0, column=20)

nextb = tk.Button(text="next")
nextb.config(width=6, height=2)
nextb.grid(row=1, column=2)

prevb = tk.Button(text="previous")
prevb.config(width=6, height=2)
prevb.grid(row=2, column=2)

randb = tk.Button(text="random")
randb.config(width=6, height=2)
randb.grid(row=3, column=2)


root.mainloop()
