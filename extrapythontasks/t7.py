letters = input("?: ")
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

print(ln)
#efboaig
#gazebo