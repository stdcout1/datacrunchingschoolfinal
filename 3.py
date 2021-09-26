import csv
from tkinter import *
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
root = Tk()
options = {}

for i in range(1980,2020):
    options[i] = 0

op1 = IntVar()
op1.set(1990)
op2 = IntVar()
op2.set(2015)

drop1 = OptionMenu(root, op1, *options.keys())
drop1.pack()
drop2 = OptionMenu(root, op2, *options.keys())
drop2.pack()
def graph():
    table = {}
    tablegta = {}
    total = {}
    for i in range(op1.get(), op2.get()):
        table[i] = 0
    tablegta = table.copy()
    total = table.copy()
    with open('CAMP.csv','r') as f:
        person = csv.reader(f)
        for i in person:
            if (i[2]) != "Ontario":
                for key,values in table.items():
                    if str(key) in i[5]:
                        table[key] += 1
            for key,values in total.items():
                if str(key) in i[5]:
                    total[key] += 1

    a = np.array(list(table.values()))/list(total.values())*100
    b = np.array(list(tablegta.values())) / list(total.values()) * 100


    plt.plot(table.keys(), a)
    plt.ylabel('% Of Kids')
    plt.xlabel('Year #')
    red_patch = mpatches.Patch(color='blue', label='Campers from outside Ontario')
    plt.legend(handles=[red_patch])
    plt.show()



Button(text = 'Graph', command = graph).pack()
lbl = Label(text = 'From what range to what range?')
lbl.pack()


root.mainloop()