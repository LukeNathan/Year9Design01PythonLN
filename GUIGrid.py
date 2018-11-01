import tkinter as tk
#
root = tk.Tk()

label = tk.Label(root, text="concentration")
label.grid(row=0, column=0, columnspan=2)

btn1 = tk.Button(root, text="1")
btn1.config(width=10, height=5)
btn1.grid(row=1, column=0)
btn1.pack

btn2 = tk.Button(root, text="2")
btn2.config(width=10, height=5)
btn2.grid(row=1, column=1)
btn2.pack

btn3 = tk.Button(root, text="3")
btn3.config(width=10, height=5)
btn3.grid(row=2, column=0)
btn3.pack

btn4 = tk.Button(root, text="4")
btn4.config(width=10, height=5)
btn4.grid(row=2, column=1)
btn4.pack


root.mainloop()
