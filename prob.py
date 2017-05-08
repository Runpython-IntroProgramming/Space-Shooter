from random import randint, shuffle

face = ['K','K','K','K','Q','Q','Q','Q','J','J','J','J']

failures = 0
trials = 100000
for i in range(trials):
    shuffle(face)
    #print(face)
    for j in range(8):
        if face[j] + face[j+1] + face[j+2] + face[j+3] == 'KKKK':
            failures += 1
            break
        if face[j] + face[j+1] + face[j+2] + face[j+3] == 'QQQQ':
            failures += 1
            break
        if face[j] + face[j+1] + face[j+2] + face[j+3] == 'JJJJ':
            failures += 1
            break
        
print((trials-failures)/trials*100,'%')
