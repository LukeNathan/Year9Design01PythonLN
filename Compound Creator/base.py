# pre alpha 0.02.6.2

import tkinter as tk
import random

root = tk.Tk()
root.geometry("1000x500")


def enter(event):
    if isinstance(event, tk.Button):
        print("true")
    print("ENTER")
    print(event.widget["text"])
    event.widget.config(foreground="red")
    # event.config(background="red")
    # loop through element list find the index and pull the name from the same index in
    # your list of names.


def free():
    func.destroy()


def form():
    if func.destroy() == true:
        func = tk.Label(root, text="Function")
        func.grid(row=1, column=16, columnspan=6)


func = tk.Label(root, text="Function")
func.grid(row=1, column=16, columnspan=6)


nextb = tk.Button(root, text="Next")
nextb.grid(row=1, column=1)
nextb.config(width=6, height=2)

prevb = tk.Button(root, text="Previous")
prevb.grid(row=2, column=1)
prevb.config(width=6, height=2)

randb = tk.Button(root, text="Random")
randb.grid(row=3, column=1)
randb.config(width=6, height=2)

formb = tk.Button(root, text="Formula", command=form)
formb.grid(row=5, column=1)
formb.config(width=6, height=2)

wordb = tk.Button(root, text="Word")
wordb.grid(row=6, column=1)
wordb.config(width=6, height=2)

freeb = tk.Button(root, text="Free", command=free)
freeb.grid(row=7, column=1)
freeb.config(width=6, height=2)


elementBtn = []
elementList = [
    "H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne",  # 10
    "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca",  # 20
    "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn",  # 30
    "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr",  # 40
    "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn",  # 50
    "Sb", "Te", "I", "Xe", "Cs", "Ba", "La", "Ce", "Pr", "Nd",  # 60
    "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb",  # 70
    "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg",  # 80
    "Ti", "Pb", "Bi", "Po", "At", "Rn", "Cs", "Fr", "Ra", "Ac",  # 90
    "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es",  # 100
    "Fm", "Md", "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt",  # 110
    "Ds", "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"]  # 120


elementRow = [
    "2", "2", "3", "3", "3", "3", "3", "3", "3", "3",  # 10
    "4", "4", "4", "4", "4", "4", "4", "4", "5", "5",  # 20
    "5", "5", "5", "5", "5", "5", "5", "5", "5", "5",  # 30
    "5", "5", "5", "5", "5", "5", "6", "6", "6", "6",  # 40
    "6", "6", "6", "6", "6", "6", "6", "6", "6", "6",  # 50
    "6", "6", "6", "6", "7", "7", "10", "10", "10", "10",  # 60
    "10", "10", "10", "10", "10", "10", "10", "10", "10", "10",  # 70
    "10", "7", "7", "7", "7", "7", "7", "7", "7", "7",  # 80
    "7", "7", "7", "7", "7", "7", "7", "8", "8", "11",  # 90
    "11", "11", "11", "11", "11", "11", "11", "11", "11", "11",  # 100
    "11", "11", "11", "11", "8", "8", "8", "8", "8", "8",  # 110
    "8", "8", "8", "8", "8", "8", "8", "8", "8", "8"]  # 120


elementCol = [
    "11", "28", "11", "12", "23", "24", "25", "26", "27", "28",  # 10
    "11", "12", "23", "24", "25", "26", "27", "28", "11", "12",  # 20
    "13", "14", "15", "16", "17", "18", "19", "20", "21", "22",  # 30
    "23", "24", "25", "26", "27", "28", "11", "12", "13", "14",  # 40
    "15", "16", "17", "18", "19", "20", "21", "22", "23", "24",  # 50
    "25", "26", "27", "28", "11", "12", "13", "14", "15", "16",  # 60
    "17", "18", "19", "20", "21", "22", "23", "24", "25", "26",  # 70
    "27", "14", "15", "16", "17", "18", "19", "20", "21", "22",  # 80
    "23", "24", "25", "26", "27", "28", "11", "11", "12", "13",  # 90
    "14", "15", "16", "17", "18", "19", "20", "21", "22", "23",  # 100
    "24", "25", "26", "27", "14", "15", "16", "17", "18", "19",  # 110
    "20", "21", "22", "23", "24", "25", "26", "27", "28"]  # 120

elementFull = [
    "Hydrogen", "Helium", "Lithium", "Beryllium", "Boron",
    "Carbon", "Nitrogen", "Oxygen", "Flourine", "Neon"]

nameLabel = []

iv = tk.Label(root, text="")
iv.grid(row=9, column=1)

for i in range(1, len(elementList) + 1, 1):
    elementBtn.append(tk.Button(root, text=elementList[i - 1]))
    elementBtn[i - 1].config(width=3, height=2)
    elementBtn[i - 1].grid(row=elementRow[i - 1], column=elementCol[i - 1])
    elementBtn[i - 1].bind("<Enter>", enter)

for i in range(1, len(elementFull) + 1, 1):
    nameLabel.append(tk.Label(root, text=elementFull[i - 1]))
    nameLabel[i - 1].grid(row=12, column=20, columnspan=10)


root.mainloop()
