
with open("day10/input.txt", "r") as file:
    data = file.readlines()

open = set({'<','(','[','{'})
match = dict({'>':'<', ')':'(', ']':'[', '}':'{'})
points = dict({'>':25137, ')':3, ']':57, '}':1197})
points2 = dict({'<':4,'(':1,'[':2,'{':3})

total = 0
scores = list()
for line in data:
    stack = ""
    corrupt = False
    score = 0
    for c in line.strip():
        if c in open:
            stack = c+stack
        else:
            if len(stack) == 0:
                total+= points[c]
                continue
            if match[c] == stack[0]:
                stack = stack[1:]
            else:
                total +=points[c]
                corrupt = True
                break
    if not corrupt and len(stack) != 0:
        for s in stack:
            score = score *5 + points2[s]
        scores.append(score)
print("part1",total)
ss = sorted(scores)
print("part2",ss[int(len(ss)/2)])

