letters = list("abcdefghijklmnopqrstuvwxyz")
values = [1,3,3,2,1,4,2,4,1,8,5,1,3,1,1,3,10,1,1,1,1,4,4,8,4,10]
dicts = dict(zip(letters,values))
counts = []
words = []
with open('wordlist.txt') as f:
    for i in f:
        count = 0
        g = i[:-1]
        if len(g) > 9:
            continue
        for e in g:
            if e == '\'':
                continue
            count += dicts[e]
        counts.append(count)
        words.append(g)
    dicts= dict(zip(words,counts))

letters = input("?: ")
lf = []
lett = ''
for i in letters:
    if i in lett:
        continue
    lett += i
ln = []
with open('wordlist.txt') as f:
    for word in f:
        g = word[:-1]
        count = 0
        if len(g) > 8:
            continue
        for i in lett:
            if i in g:
                if g.count(i) == letters.count(i):
                    count += g.count(i)
                else:
                    count += 1
        if count == len(g):
            ln.append(g)
lg = []
for i in ln:
    lf.append(dicts[i])
for i in range(lf.count(max(lf))):
    print(ln[lf.index(max(lf))])
    ln.pop(lf.index(max(lf)))
    lf.pop(lf.index(max(lf)))
