f = open('words', 'r')
text = list(f.read())
import string
ntl = 0
mydict = {}
alphab = list(string.ascii_lowercase)
for j in range(len(alphab)):
    for i in range(len(text)):
        if text[i] == alphab[j]:
            ntl = ntl + 1
            try:
                mydict[alphab[j]] = mydict[alphab[j]] + 1
            except KeyError:
                mydict[alphab[j]] = 1
for key in mydict:
    gro = key + ':'
    print(gro, mydict[key]/ntl)
