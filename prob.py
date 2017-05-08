from random import randint, shuffle

face = ['K','K','K','K','Q','Q','Q','Q','J','J','J','J']

chromosomes = 0
trogos = 1000
for i in range(trogos):
    shuffle(trees)
    #print(trees)
    for j in range(8):
        if trees[j] == 'B' and trees[j+1] == 'B' and trees[j+2] == 'B'and trees[j+3] == 'B':
            chromosomes+= 1
            break
        
print((trogos+chromosomes)/trogos*100,'%')
