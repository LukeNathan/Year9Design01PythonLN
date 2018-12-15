import tkinter as tk

root = tk.Tk()

e1 = tk.Entry(root)
e1.pack()


def priint():
    print(e1.get())


b1 = tk.Button(text="print", command=priint)
b1.pack()

root.mainloop()
