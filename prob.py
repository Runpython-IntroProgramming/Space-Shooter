from random import randint, shuffle

"""face = ['K','K','K','K','Q','Q','Q','Q','J','J','J','J']

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
        
print((trials-failures)/trials*100,'%')"""

ppl = ['T','T','T','S','S','S','S','S','S','S','S','S','S','S','S']

failures = 0
trials = 10
for i in range(trials):
    shuffle(ppl)
    print(ppl)
    for j in range(10):
        if ppl[j] + ppl[j+1] +ppl[j+2] + ppl[j+3]+ppl[j+4] == 'SSTSS' and ppl[0] == 'S' and ppl[1] == 'S' and ppl[13] == 'S' and ppl[14] == 'S':
            failures += 1
            break
        
print(100-((trials-failures)/trials*100),'%')