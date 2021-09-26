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
    cool = dict(zip(words,counts))
ret = input('?: ')
print (cool)