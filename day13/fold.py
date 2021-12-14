with open("day13/input.txt", "r") as file:
    data = file.readlines()

with open("day13/fold.txt", "r") as file:
    fold = file.readlines()

dots = set()
dl = list()
maxy = 0
maxx = 0
for line in data:
    line = line.strip()
    ss = line.split(",")
    if int(ss[1]) > maxy:
        maxy = int(ss[1])
    if int(ss[0]) > maxx:
        maxx = int(ss[0])
    dl.append((ss[1],ss[0]))
    dots.add(ss[1]+','+ss[0])

print(fold)
print(dots)
print(len(dots))
print(maxx, maxy)
maxx +=1
maxy +=1
for line in fold:
    line = line.strip()
    ss = line.split("=")
    if 'x' in ss[0]:
        print("fold x", ss[1])
        for y in range(maxy+1):
            for x in range(int(ss[1])+1,maxx+1):  
                dot = str(y)+','+str(x)
                if dot in dots:
                    newdot = str(y)+','+str(int(ss[1])*2 - x)
                    #print(dot, newdot)
                    dots.add(newdot)
                    dots.remove(dot)
        maxx = int(ss[1])

    if 'y' in ss[0]:
        print("fold y", ss[1])
        for y in range(int(ss[1])+1, maxy+1):
            for x in range(maxx+1):  
                dot = str(y)+','+str(x)
                if dot in dots:
                    newdot = str(int(ss[1])*2 - y)+','+str(x)
                    #print(dot, newdot)
                    dots.add(newdot)
                    dots.remove(dot)
        maxy = int(ss[1])
    #print(dots)
    #print("dots",len(dots))

for y in range(maxy+1):
    m = [' '] *(maxx+1)
    for x in range(maxx+1):
        dot = str(y)+','+str(x) 
        if dot in dots:
            m[x] = '*'
    print(m)
