import tkinter as tk

root = tk.Tk()


def show(event):
    print("Entered")


def unshow(event):
    print("exited")


button = tk.Button(text="hi")
button.pack()

button.bind("<Enter>", show)
button.bind("<Leave>", unshow)

root.mainloop()
