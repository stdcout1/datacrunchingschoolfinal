letters = input("?: ")
ln = []
with open('wordlist.txt') as f:
    for word in f:
        g = word[:-1]
        for i in g:
            if i in letters:
                pass
            else:
                break
        for i in letters:
            if letters.count(i) != g.count(i):
                valid = False
                break
        if valid:
            ln.append(g)
print(ln)
#efboaig
#gazebo