import bisect

def findrisks(score, y, x, matrix,risks):
    if y < 0 or x < 0 or y == len(risks) or x == len(risks[y]):
        return -1
    if risks[y][x] == -1:
        risks[y][x] = score + matrix[y][x]
    elif score + matrix[y][x] < risks[y][x]:
        risks[y][x] = score + matrix[y][x]
    else:
        return -1
    return risks[y][x]

with open("day15/input.txt", "r") as file:
    data = file.readlines()
matrix = list()
risks = list()
for line in data:
    line = list(map(lambda x: int(x),line.strip()))
    matrix.append(list(line))
    risks.append(list([-1]*len(line)))

print(matrix)
print(risks)
heads = list()
heads.append((0,(0,0)))
while len(heads) != 0:
    #print(heads)
    h = heads[0]
    print(h)
    heads = heads[1:]
    score = h[0]
    y = h[1][0]
    x = h[1][1]
    if y == len(matrix)-1 and x == len(matrix[0])-1:
        print("end!", h)
        break

    s = findrisks(score, y, x+1, matrix,risks)
    if s != -1:
        bisect.insort(heads, (s, (y,x+1)))
    s = findrisks(score, y+1, x, matrix,risks)
    if s != -1:
        bisect.insort(heads, (s, (y+1,x)))
    s = findrisks(score, y, x-1, matrix,risks)
    if s != -1:
        bisect.insort(heads, (s, (y,x-1)))
    s = findrisks(score, y-1, x, matrix,risks)
    if s != -1:
        bisect.insort(heads, (s, (y-1,x)))