import copy

def addpath(f, t, path):
    if f in path:
        path[f].append(t)
    else:
        path[f] = list([t])

with open("day12/input.txt", "r") as file:
    data = file.readlines()

path = dict()
for line in data:
    line = line.strip()
    sp = line.split("-")
    print(sp)
    addpath(sp[0], sp[1], path)
    addpath(sp[1], sp[0], path)
print(path)
pending = list()
for p in path['start']:
    pending.append((['start', p],set(['start', p])))

counter = 0
while len(pending)!=0:
    p = pending[0]
    pending = pending[1:]
    last = p[0][-1]
    #print(sofar)
    if last == "end":
        counter +=1
        #print(counter)
        continue

    for next in path[last]:
        sofar = copy.deepcopy(p[0])
        visited = copy.deepcopy(p[1])
        if next[0].islower() and next in visited:
            continue
        sofar.append(next)
        visited.add(next)
        pending.append((sofar, visited)) 

print(counter)