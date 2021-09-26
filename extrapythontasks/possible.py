word = 'nasir'
words = []
with open('wordlist.txt') as f:
    for i in f:
        y = i[:-1]
        for e in word:
            count = 0
            if e in i :
                count += i.count(e)
            if count == len(word):
                words.append(e)
print (count)
print (words)
