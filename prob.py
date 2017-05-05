from random import randint, shuffle

trees = ['M','M','M','O','O','O','O','B','B','B','B','B']

chromosomes = 0
trogos = 1000
for i in range(trogos):
    shuffle(trees)
    #print(trees)
    for j in range(9):
        if trees[j] == 'B' and trees[j+1] == 'B' and trees[j+2] == 'B'and trees[j+3] == 'B':
            chromosomes+= 1
            break
        
print((trogos+chromosomes)/trogos*100,'%')
