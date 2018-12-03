import tkinter as tk

root = tk.Tk()
root.geometry("1000x500")


def quit():
    root.destroy()


def start():
    quitb.destroy()
    startb.destroy()
    name.destroy()


name = tk.Label(text="Compound Creator")
name.config(font=("Roboto", 44), height=5)
name.pack()

startb = tk.Button(root, text="Start", command=start)
startb.config(width=15, height=5)
startb.pack()

quitb = tk.Button(root, text="Quit", command=quit)
quitb.config(width=15, height=5)
quitb.pack()


root.mainloop()
