def findsize(y, x):
    if y < 0 or x < 0 or y == len(ints) or x == len(ints[y]):
        return 
    ints[y][x] += 1
    if ints[y][x] == 10:
        findsize(y+1,x)
        findsize(y-1,x)
        findsize(y,x+1)
        findsize(y,x-1)

        findsize(y+1,x+1)
        findsize(y+1,x-1)
        findsize(y-1,x+1)
        findsize(y-1,x-1)
    
with open("day11/input.txt", "r") as file:
    data = file.readlines()

ints = list()
for i, _ in enumerate(data):
    ints.append(list(map(lambda x: int(x), data[i].strip())))

print(ints)
counter = 0

i = 1
#for i in range(100):
while True:
    c=0
    for y in range(len(ints)):
        for x in range(len(ints[y])):  
                findsize(y, x)
                
    for y in range(len(ints)):
        for x in range(len(ints[y])):  
            if ints[y][x] >= 10:
                c += 1
                ints[y][x] = 0
    print(i, c)
    if c == 100:
        print(i)
        break
    counter += c
    i+=1
for y in range(len(ints)):
    print(ints[y])
print(counter)
