import tkinter as tk

root = tk.Tk()


def show(event):
    ent = tk.Label(root, text="Entered")
    ent.pack()
    if ent.winfo_exists() == True:
        ent.destroy()
    ent = tk.Label(root, text="Entered")
    ent.pack()


def unshow(event):
    ex = tk.Label(root, text="Exited")
    ex.pack()


button = tk.Button(text="hi")
button.pack()

button.bind("<Enter>", show)
button.bind("<Leave>", unshow)

root.mainloop()
