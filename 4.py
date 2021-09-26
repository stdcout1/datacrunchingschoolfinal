import csv
from tkinter import *
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import datetime as dt
root = Tk()
options = {}

for i in range(1980,2020):
    options[i] = 0

op1 = IntVar()
op1.set(2000)

drop1 = OptionMenu(root, op1, *options.keys())
drop1.pack()

def graph():
    table = {}
    for i in range(0, 18):
        table[i] = 0
    with open('CAMP.csv','r') as f:
        person = csv.reader(f)
        for i in person:
            area = i[5].split(sep= ' ')[1]
            if 'VO' in area or 'RA' in area or 'FR' in area or 'RO' in area:
                pass
            else:
                continue
            if i[0] == "":
                continue
            dobyear  = int(i[0].split(sep='/')[2])
            dobdate = int(i[0].split(sep='/')[0])
            dobmonth = int(i[0].split(sep='/')[1])



            ret = dt.date(int(i[5].split(sep= ' ')[0]),7,1)
            dob = dt.date(dobyear, dobmonth, dobdate)
            ageofret = (ret-dob)

            if ageofret.days < 0 or int(ageofret.days/365) > 18:
                continue
            curage = ageofret.days/365

            for key,values in table.items():
                if int(key) == int(curage) and str(op1.get()) in i[5]:
                    table[key] += 1

    print(table)

    plt.plot(table.keys(), table.values(), '-ok')
    plt.ylabel('Number of Campers')
    plt.xlabel('Age')
    red_patch = mpatches.Patch(color='blue', label='Campers age at which they retire at')
    plt.legend(handles=[red_patch])
    scale_factor = 1.5

    xmin, xmax = plt.xlim()
    ymin, ymax = plt.ylim()

    plt.xlim(xmin * scale_factor, xmax * scale_factor)
    plt.ylim(ymin * scale_factor, ymax * scale_factor)
    plt.show()



Button(text = 'Graph', command = graph).pack()
lbl = Label(text = 'What year?')
lbl.pack()


root.mainloop()