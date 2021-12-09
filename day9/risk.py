def checklow(data, y, x):
    pos = data[y][x]
    if 0 <= y-1:
        if data[y-1][x] <= pos:
            return False

    if 0<= x-1:
        if data[y][x-1] <= pos:
            return False

    if x+1 < len(data[y]):
        if data[y][x+1] <= pos:
            return False

    if  y+1 < len(data) :
        if data[y+1][x] <= pos:
            return False            
    return True

with open("day9/input.txt", "r") as file:
    data = file.readlines()
risk = 0
for y in range(len(data)):
    data[y] = data[y].strip()
    for x in range(len(data[y])):
        if checklow(data, y, x):
            risk += int(data[y][x])+1
            #print(data[y][x], y,x,risk)

print(risk)

# part 2
def findsize(y, x):
    if y < 0 or x < 0 or y == len(data) or x == len(data[y]):
        return 0
    if data[y][x] == '*':
        return 0
    data[y][x] = '*'
    return 1+ findsize(y+1,x)+findsize(y-1,x)+findsize(y,x+1)+findsize(y,x-1)

sizes = list()
for y in range(len(data)):
    data[y] = list(data[y].replace('9','*'))

for y in range(len(data)):
    for x in range(len(data[y])):   
        if data[y][x] != "*":
            sizes.append(findsize(y, x))

print(sorted(sizes))