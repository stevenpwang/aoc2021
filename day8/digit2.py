def count(arr):
    counter = dict()
    for num in arr:
        for c in num:
            if c in counter:
                counter[c]+=1
            else:
                counter[c] = 1
    return counter

def remove(arr, ag):
    filtered = list()
    for num in arr:
        for r in ag:
            num = num.replace(r, "")
        filtered.append(num)
    return filtered

def findmappings(og):
    mapping = dict()
    filtered = list()
    arr = og

    # find easy four
    for num in arr:
        if len(num) not in set([2,3,4,7]):
            filtered.append(num)
    arr = filtered

    # remove a and g
    counter = count(arr)
    ag = list()
    for key, val in counter.items():
        if val == len(arr):
            ag.append(key) # a or g
    #print("ag", ag)
    arr = remove(arr, ag)
    
    # find d among length 3, remove d
    len3 = list()
    for num in arr:
        if len(num) == 3:
            len3.append(num)
    clen3 = count(len3)
    for key, val in clen3.items():
        if val == len(len3):
            mapping['d'] = key
            arr = remove(arr, [key])
            break

    # remove 0 which is the longest str from arr
    filtered = list()
    for num in arr:
        if len(num)!= 7 - len(mapping) - 2:
            filtered.append(num)
    arr = filtered

    # c3 (c appeared 3 times) e2 f4 b3, found e and f, remove 2 amd 6 which only has e in their length
    counter = count(arr)
    for key, val in counter.items():
        if val == 2:
            mapping['e'] = key
        if val == 4:
            mapping['f'] = key

    # the only one left of length 3 is 9, the common segment between 3 and 5 is f
    # remove 2 and 6
    filtered = list()
    for num in arr:
        if mapping['e'] not in num and len(num)!=3:
            filtered.append(num)
    arr = filtered

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

easy = dict()
easy[2] = 1
easy[3] = 7
easy[4] = 4
easy[7] = 8

sd = dict()
sd["bcef"] = 0
sd["cde"] = 2
sd["cdf"] = 3
sd["bdf"]= 5
sd["bdef"] = 6
sd["bcdf"] = 9

total = 0
for line in data:
    sl = line.split("|") 
    ten = sl[0].split()
    four = sl[1].split()
    mapping = findmappings(ten)
    reverse = dict()
    for key, val in mapping.items():
        reverse["".join(sorted(val))] = key
    #print(reverse)
    out = ""
    for f in four:
        if len(f) in easy:
            out+=str(easy[len(f)])
        else:
            decoded = ""
            for c in f:
                if c in reverse:
                    decoded += reverse[c]
            out+= str(sd["".join(sorted(decoded))])
    
    print(out)
    total+=int(out)
print(total)
