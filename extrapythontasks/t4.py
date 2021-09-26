import csv
import json
students =[]
with open('HONOUR.CSV') as f:
    file = csv.reader(f)

    for i in file:
        if "English" in i:
            continue
        g = (i[2:])
        avg = 0
        for b in g:
            avg += int(b)
        avg = avg/len(g)
        if avg >= 80:
            students.append(i[0] + ' ' +i[1])

    print ("The students who got honour role are: " + str(students) + ' \n' + "There are a total of: " + str(len(students)))

marks = {}
beta = []
winners = {}
winnern = []
subjects = ['English', 'Math', 'Geography', 'Science', 'Gym', 'History', 'Art', 'Music']
for i in subjects:
    beta = []
    with open('HONOUR.CSV') as f:
        file = csv.reader(f)
        for e in file:
            if "Last" in e:
                continue
            g = (e[2:])
            if not beta:
                beta.append(0)
            beta.append(int(g[subjects.index(i)]))
    print (beta)
    marks[i] = beta

for key,value in marks.items():
    winners[key] = value.index(max(value))
    print (winners)
subjects = []
with open('honour.csv') as f:
    file = csv.reader(f)
    count = 0
    for i in file:
        for key,value in winners.items():
            if value == count:
                print (count)
                winnern.append(i[0] + ", " + i[1])
                subjects.append(key)
        count += 1
winnern = dict((zip(subjects,winnern)))
print ("The winners of the subject award is: " + str(winnern))
