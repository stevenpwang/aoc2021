with open("day4/input.txt", "r") as file:
    data = file.readlines()
line = data[0]
nums = line.split(',')
print(nums)

bs = list()
b = list()

ms = list()
with open("day4/board.txt", "r") as file:
    data = file.readlines()
    for line in data:
        if line == "\n" :
            b = list()
            continue
        row = line.split()
        b.append(row)
        if len(b) == len(b[0]) :
            bs.append(b)
            ms.append([[0 for x in range(len(b))] for y in range(len(b[0]))] )
            #print(b)

print(len(bs),len(ms))

def checkBrow(m, x, b):
    y = 0
    while y < len(m[x]):
        if m[x][y] == 0:
            return -1
        y+=1
    return getsum(m,b)

def checkBcol(m, y, b):
    x = 0
    while x < len(m):
        if m[x][y] == 0:
            return -1            
        x+=1
    result = list()
    for x in range(len(b)):
        result.append(b[x][y])
    return getsum(m,b)

def getsum(m,b):

    x = 0
    s = 0
    while x < len(m):
        y = 0
        while y < len(m[x]):
            if m[x][y]== 0:
                s+=int(b[x][y])
            y+=1
        x+=1
    return s

def findwinners(nums, bs, ms):
    won = set()
    scores = list()
    for i in nums:
        for th, b in enumerate(bs):
            if th in won:
                continue
            for x, r in enumerate(b):
                for y, n in enumerate(r):
                    if n == i:
                        ms[th][x][y] = 1

                        row = checkBrow(ms[th], x, b)
                        col = checkBcol(ms[th], y, b)
                        if row != -1 or col != -1:
                            won.add(th)
                            if row !=-1:
                                scores.append(row*int(i))
                            else:
                                scores.append(col*int(i))
    print(scores[-1])


findwinners(nums, bs, ms)
