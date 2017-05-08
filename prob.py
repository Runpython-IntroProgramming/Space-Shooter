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
ko=0
for i in range(trials):
    shuffle(ppl)
    print(ppl)
    if ppl[0] == 'T' or ppl[1] == 'T' or ppl[13] == 'T' or ppl[14]=='T':
        failures+=1
        ko=1
    if ko == 0:
        for j in range(13):
            if ppl[j] + ppl[j+1] == 'TT':
                failures += 1
                ko=2
                break
    if ko==0:
        for j in range(12):
            if ppl[j] + ppl[j+1]+ppl[j+2] == 'TST':
                failures += 1
                break
                
        

        
print((trials-failures)/trials*100,'%')
