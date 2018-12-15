import tkinter as tk

root = tk.Tk()

button1 = tk.Button(root, text="button1")
button1.pack()

button2 = tk.Button(root, text="button2")
button2.pack()

button1.bind("<Enter>", enter)
button2.bind("<Enter>", enter)


root.mainloop()
