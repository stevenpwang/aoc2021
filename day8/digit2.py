def count(arr):
    counter = dict()
    for c in "".join(arr):
        if c in counter:
            counter[c]+=1
        else:
            counter[c] = 1
    return counter

def replace(num, ag):
    for r in ag:
        num = num.replace(r, "")
    return num

def remove(arr, ag):
    filtered = list(map(lambda num: replace(num, ag), arr))
    return filtered

def findmappings(og):
    mapping = dict()
    arr = og
    
    # find easy four
    arr = list(filter(lambda num: len(num) not in set([2,3,4,7]) , arr))
    
    # remove a and g
    counter = count(arr)
    ag = list()
    for key, val in counter.items():
        if val == len(arr):
            ag.append(key) # a or g
    #print("ag", ag)
    arr = remove(arr, ag)
    
    # find d among length 3, remove d
    len3 = list(filter(lambda num: len(num) == 3, arr))
    clen3 = count(len3)
    for key, val in clen3.items():
        if val == len(len3):
            mapping['d'] = key
            arr = remove(arr, [key])
            break

    # remove 0 which is the longest str from arr
    arr = list(filter(lambda num: len(num)!= 7 - len(mapping) - 2, arr))

    # c3 (c appeared 3 times) e2 f4 b3, found e and f, remove 2 amd 6 which only has e in their length
    counter = count(arr)
    for key, val in counter.items():
        if val == 2:
            mapping['e'] = key
        if val == 4:
            mapping['f'] = key

    # the only one left of length 3 is 9, the common segment between 3 and 5 is f
    # remove 2 and 6
    arr = list(filter(lambda num: mapping['e'] not in num and len(num)!=3, arr))

    # remove f
    # distinguish c and b by checking their number of appearance in step 2. 
    arr = remove(arr, [mapping['f']])
    if clen3[arr[0]] == 1:
        mapping['b'] = arr[0] 
        mapping['c'] = arr[1]
    else:
        mapping['b'] = arr[1] 
        mapping['c'] = arr[0]

    return mapping

with open("day8/input.txt", "r") as file:
    data = file.readlines()

easy = dict({2:1, 3:7, 4:4, 7:8})
# map segment pattern to digit
sd = dict({"bcef": 0, "cde":2, "cdf": 3, "bdf": 5, "bdef": 6, "bcdf":9})

total = 0
for line in data:
    sl = line.split("|") 
    ten, four = sl[0].split(), sl[1].split()
    mapping = findmappings(ten)
    reverse = dict()
    for key, val in mapping.items():
        reverse["".join(sorted(val))] = key
    #print(reverse)
    out = 0
    for f in four:
        i = -1
        if len(f) in easy:
            i = easy[len(f)]
        else:
            decoded = ""
            for c in f:
                if c in reverse:
                    decoded += reverse[c]
            i = sd["".join(sorted(decoded))]
        out = out*10 + i
    print(out)
    total+=out
print(total)
