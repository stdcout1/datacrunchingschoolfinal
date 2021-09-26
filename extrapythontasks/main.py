left = "samie"
right = "nasir"
ln = 0
rn = 0
with open("wordlist.txt") as f:
    for word in f:
        count = 1
        for i in left:
            if i in word:
                count += word.count(i)
        if count == len(word):
            ln += 1
            #print (word) #Words you can type with your left hand
        count = 1
        for i in right:
            if i in word:
                count += word.count(i)
        if count == len(word):
            rn += 1
            # print (word) #Words you can type with your right hand

print ("The amount of words you can type with your right hand is: " + str(rn))
print ("The amount of words you can type with your left hand is: " + str(ln))