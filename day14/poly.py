from collections import Counter

with open("day14/input.txt", "r") as file:
    data = file.readlines()

state = "PFVKOBSHPSPOOOCOOHBP"
trans = dict()
for line in data:
    ss = line.strip().split(" -> ")
    trans[ss[0]] =ss[1]

for r in range(10):
    ns = ""
    for i in range(len(state)-1):
        two = state[i:i+2]
        if two in trans:
            ns += two[0]+trans[two]
        else:
            ns+=two[0]
    ns += state[-1]
    state = ns
    print(state)

counter = Counter(state)
print(counter)
#Counter({'V': 3525, 'H': 3125, 'K': 2320, 'N': 2303, 'F': 1961, 'S': 1856, 'C': 1816, 'B': 1081, 'O': 882, 'P': 588})

