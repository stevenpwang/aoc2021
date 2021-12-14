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
    if sp[1] != 'start':
        addpath(sp[0], sp[1], path)
    if sp[0] != 'start':
        addpath(sp[1], sp[0], path)

pending = list()
for p in path['start']:
    pending.append((['start', p],set(['start', p]),False))

path.pop('start')
path.pop('end')
print(path)

counter = 0
while len(pending)!=0:
    p = pending[0]
    pending = pending[1:]
    last = p[0][-1]
    print(p[0])
    if last == "end":
        counter +=1
        #print(counter)
        continue

    for next in path[last]:
        sofar = copy.deepcopy(p[0])
        visited = copy.deepcopy(p[1])
        twice = p[2]
        if next[0].islower() and next in visited:
            if twice == False:
                twice = True
            else:
                continue
        sofar.append(next)
        visited.add(next)
        pending.append((sofar, visited, twice)) 

print(counter)