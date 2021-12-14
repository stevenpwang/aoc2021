with open("day14/input.txt", "r") as file:
    data = file.readlines()

state = "PFVKOBSHPSPOOOCOOHBP"
trans = dict()
for line in data:
    ss = line.strip().split(" -> ")
    trans[ss[0]] =ss[1]

paircount = dict()

for i in range(len(state)-1):
    two = state[i:i+2]
    if two not in paircount:
        paircount[two] = 0
    paircount[two]+=1

for r in range(40):
    #new pair count
    npc = dict()
    for two in paircount.keys():
        if two in trans:
            newc = trans[two]
            if two[0]+newc not in npc:
                npc[two[0]+newc] = 0
            npc[two[0]+newc] += paircount[two]
            if newc+two[1] not in npc:
                npc[newc+two[1]] = 0
            npc[newc+two[1]] += paircount[two]
    paircount = npc

#print(paircount)
ccount = dict()
for key in paircount.keys():
    for k in key:
        if k not in ccount:
            ccount[k]=0
        ccount[k]+=paircount[key]

# first and last char are only counted once
ccount[state[0]]+=1
ccount[state[-1]]+=1

# now all characters are double counted
for key in ccount.keys():
    ccount[key] = int(ccount[key]/2)
sl = sorted(ccount.items(), key=lambda x: x[1])
print(sl[-1][1] - sl[0][1])