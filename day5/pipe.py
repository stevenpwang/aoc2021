
matrix = [[0 for x in range(1000)] for y in range(1000)]
with open("day5/input.txt", "r") as file:
    data = file.readlines()

for line in data:
    sp = line.split(" ")
    start = sp[0]
    end = sp[2]
    print(start, end)
    ss = start.split(",")
    es = end.split(",")
    sx = int(ss[0])
    sy = int(ss[1])
    ex = int(es[0])
    ey = int(es[1])
    if sx == ex:
        for i in range(min(sy,ey), max(sy,ey)+1):
            matrix[sx][i] += 1
    elif sy == ey:
        for i in range(min(sx, ex), max(sx, ex)+1):
            matrix[i][sy] += 1
    else:
        for i in range(abs(sx - ex)+1):
            if ex < sx:
                mx = -i
            else:
                mx = i
            x = sx + mx

            if ey < sy:
                my = -i
            else:
                my = i
            y = sy + my
            matrix[x][y] +=1

counter =0
for row in matrix:
    #print(row)
    for col in row:
        if col >1:
            counter+=1
print(counter)


