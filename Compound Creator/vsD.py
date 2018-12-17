
import tkinter as tk
import random

root = tk.Tk()
root.geometry("750x500")
root.title("Compound Creator")

name = tk.StringVar()
nameLabel = tk.Label(root, textvariable=name)
nameLabel.grid(row=12, column=20, columnspan=10)

box = tk.StringVar()
entr = tk.Entry(root, textvariable=box)
entr.grid(row=20, column=21, columnspan=10)
entr.config(state='disabled')


def enter(event):
    # if isinstance(event, tk.Button):
    #     for i in range(1, len(elementBtn) + 1, 1)
    #         nameLabel[elementBtn.index(i - 1)].grid()
    #         print("works")
    print("ENTER")
    print(event.widget["text"])
    event.widget.config(foreground="red")
    name.set(elementFull[elementList.index(event.widget["text"])])


def exit(event):
    event.widget.config(foreground="black")


def type(event):
    box.set(box.get() + event.widget["text"])
    h1 = tk.Button(root, text="1", command=t1)
    h1.grid(row=5, column=30)
    h2 = tk.Button(root, text="2", command=t2)
    h2.grid(row=6, column=30)
    h3 = tk.Button(root, text="3", command=t3)
    h3.grid(row=7, column=30)
    h4 = tk.Button(root, text="4", command=t4)
    h4.grid(row=5, column=31)
    h5 = tk.Button(root, text="5", command=t5)
    h5.grid(row=6, column=31)
    h6 = tk.Button(root, text="6", command=t6)
    h6.grid(row=7, column=31)
    h7 = tk.Button(root, text="7", command=t7)
    h7.grid(row=5, column=32)
    h8 = tk.Button(root, text="8", command=t8)
    h8.grid(row=6, column=32)
    h9 = tk.Button(root, text="9", command=t9)
    h9.grid(row=7, column=32)


def submitc():
    print(entr.get())
    if entr.get() == "H2O":
        print("water")
        waterl = tk.Label(root, text="Water")
        waterl.grid(row=3, column=16, columnspan=5)
    if entr.get() == "CO2":
        print("carbon dioxide")
        carbl = tk.Label(root, text="Carbon Dioxide")
        carbl.grid(row=3, column=16, columnspan=5)
    if entr.get() == "C6H12O6":
        glucl = tk.Label(root, text="Glucose")
        glucl.grid(row=3, column=16, columnspan=5)
    if entr.get() == "C6H8O7":
        print("citric acid")
        citrl = tk.Label(root, text="Citric Acid")
        citrl.grid(row=3, column=16, columnspan=5)
    if entr.get() == "NH3":
        print("ammonia")
        citrl = tk.Label(root, text="Ammonia")
        citrl.grid(row=3, column=16, columnspan=5)
    box.set("")


def t1():
    box.set(box.get() + "1")


def t2():
    box.set(box.get() + "2")


def t3():
    box.set(box.get() + "3")


def t4():
    box.set(box.get() + "4")


def t5():
    box.set(box.get() + "5")


def t6():
    box.set(box.get() + "6")


def t7():
    box.set(box.get() + "7")


def t8():
    box.set(box.get() + "8")


def t9():
    box.set(box.get() + "9")


def clear():
    box.set("")


def free():
    func.grid_remove()


def quit():
    root.destroy()


def word():
    func.grid_remove()
    func1.grid_remove()
    wordl.grid()


def collapse():
    nextb.grid_remove()
    prevb.grid_remove()
    randb.grid_remove()
    formb.grid_remove()
    wordb.grid_remove()
    freeb.grid_remove()
    listb.grid_remove()
    menub.grid_remove()
    quitb.grid_remove()
    xquit.grid_remove()
    xshow.grid()


def show():
    nextb.grid()
    prevb.grid()
    randb.grid()
    formb.grid()
    wordb.grid()
    freeb.grid()
    listb.grid()
    menub.grid()
    quitb.grid()
    xshow.grid_remove()
    xquit.grid(row=1, column=6)


xshow = tk.Button(root, text=">", command=show)
xshow.grid(row=1, column=6)


def default():
    xshow.grid_remove()


func = tk.Label(root, text="H2O")
func.grid(row=1, column=16, columnspan=6)

func2 = tk.Label(root, text="C6H12O6")
func2.grid(row=1, column=16, columnspan=6)
func2.grid_remove()

wordl = tk.Label(root, text="Water")
wordl.grid(row=1, column=16, columnspan=6)
wordl.grid_remove()

wordl1 = tk.Label(root, text="Glucose")
wordl1.grid(row=1, column=16, columnspan=6)
wordl1.grid_remove()


def prev():
    func2.grid_remove()
    func.grid()


def next():
    func2.grid()
    func.grid_remove()


def form():
    func.grid()


nextb = tk.Button(root, text="Next", command=next)
nextb.grid(row=1, column=1)
nextb.config(width=6, height=2)

prevb = tk.Button(root, text="Previous", command=prev)
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

listb = tk.Button(root, text="List")
listb.grid(row=9, column=1)
listb.config(width=6, height=2)

menub = tk.Button(root, text="Menu")
menub.grid(row=11, column=1)
menub.config(width=6, height=2)

quitb = tk.Button(root, text="Quit", command=quit)
quitb.grid(row=12, column=1)
quitb.config(width=6, height=2)

xquit = tk.Button(root, text="<", command=collapse)
xquit.grid(row=1, column=6)

clearb = tk.Button(root, command=clear, text="Clear")
clearb.grid(row=19, column=29, columnspan=3)
clearb.config(height=1, width=5)

submitb = tk.Button(root, text="Submit", command=submitc)
submitb.grid(row=20, column=29, columnspan=3)
submitb.config(height=1, width=5)

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
    "Tl", "Pb", "Bi", "Po", "At", "Rn", "Cs", "Fr", "Ra", "Ac",  # 90
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
    "Hydrogen", "Helium", "Lithium", "Beryllium", "Boron",  # 5
    "Carbon", "Nitrogen", "Oxygen", "Flourine", "Neon",  # 10
    "Sodium", "Magnesium", "Aluminum", "Silicon", "Phosphorus",  # 15
    "Sulfur", "Chlorine", "Argon", "Potassium", "Calcium",  # 20
    "Scandium", "Titanium", "Vanadium", "Chromium", "Manganese",  # 25
    "Iron", "Cobalt", "Nickel", "Copper", "Zinc",  # 30
    "Gallium", "Germanium", "Arsenic", "Selenium", "Bromine",  # 35
    "Krypton", "Rubidium", "Strontium", "Yttrium", "Zirconium",  # 40
    "Niobium", "Molybdenum", "Technetium", "Ruthenium", "Rhodium",  # 45
    "Palladium", "Silver", "Cadmium", "Indium", "Tin",  # 50
    "Antimony", "Tellurium", "Iodine", "Xenon", "Cesium",  # 55
    "Barium", "Lanthanum", "Cerium", "Praseodymium", "Neodymium",  # 60
    "Promethium", "Samarium", "Europium", "Gadolinium", "Terbium",  # 65
    "Dysprosium", "Holmium", "Erbium", "Thulium", "Ytterbium",  # 70
    "Lutetium", "Hafnium", "Tantalum", "Tungsten", "Rhenium",  # 75
    "Osmium", "Iridium", "Platinum", "Gold", "Mercury",  # 80
    "Thallium", "Lead", "Bismuth", "Polonium", "Astatine",  # 85
    "Radon", "", "Francium", "Radium", "Actinium", "Thorium",  # 90
    "Protactinium", "Uranium", "Neptunium", "Plutonium", "Americium",  # 95
    "Curium", "Berkelium", "Californium", "Einsteinium", "Fermium",  # 100
    "Mendelevium", "Nobelium", "Lawrencium", "Rutherfordium", "Dubnium",  # 105
    "Seaborgium", "Bohrium", "Hassium", "Meitnerium", "Darmstadtium",  # 110
    "Roentgenium", "Copernicium", "Nihonium", "Flerovium", "Moscovium",  # 115
    "Livermorium", "Tennessine", "Oganesson"]  # 118

#nameLabel = []


for i in range(1, len(elementList) + 1, 1):
    elementBtn.append(tk.Button(root, text=elementList[i - 1]))
    elementBtn[i - 1].config(width=3, height=2)
    elementBtn[i - 1].grid(row=elementRow[i - 1], column=elementCol[i - 1])
    elementBtn[i - 1].bind("<Enter>", enter)

for i in range(1, len(elementFull) + 1, 1):
    #nameLabel.append(tk.Label(root, text=elementFull[i - 1]))
    #nameLabel[i - 1].grid(row=12, column=20, columnspan=10)
    elementBtn[i - 1].bind("<Enter>", enter)
    elementBtn[i - 1].bind("<Leave>", exit)
    elementBtn[i - 1].bind("<Button-1>", type)

#nameLabel[i - 1].grid_remove()

root.mainloop()
