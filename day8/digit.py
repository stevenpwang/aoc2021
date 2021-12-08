with open("day8/input.txt", "r") as file:
    data = file.readlines()

easy = dict()
easy[2] = 1
easy[3] = 7
easy[4] = 4
easy[7] = 8

counter = 0
for line in data:
    four = line.split("|")[1].split()
    print(four)
    out = ""
    for f in four:
        if len(f) in easy:
            counter+=1
            out+=str(easy[len(f)])
        else:
            out+=f
        out+=" "
    print(out)
print(counter) #part1: 452