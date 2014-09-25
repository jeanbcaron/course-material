f = open('words', 'r')
nbe = 0
for line in f:
    for i in range(len(line)):
        if line[i] == 'e':
            nbe = nbe+1
print(nbe)
