import tkinter as tk


root = tk.Tk()

elementList = ["H", "He", "Li", "Be" "C" "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar"]
elementxLoc = ["2", "2", "3", "3", "3", "3", "3", "3", "3", "3", "4", "4", "4", "4", "4", "4", "4", "4"]
elemtnyLoc = ["1", "18", "1", "2", "13", "14", "15", "16", "17", "18", "1", "2", "13", "14", "15", "16", "17", "18"]


buttonList = []
locList = []

for i in range(0, 3, 1):
    buttonList.append(tk.Button(root, text=elementList[i])

for i in range(0, 3, 1):
    locList.append(tk.Button(root, text=elementxLoc[i])
