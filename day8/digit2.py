from collections import Counter

def remove(arr, ag):
    filtered = list(map(lambda num: ''.join(set(num) - set(ag)), arr))
    return filtered

def findmappings(arr):
    mapping = dict()

    # find easy four
    arr = list(filter(lambda num: len(num) not in set([2,3,4,7]) , arr))
    
    # remove a and g
    counter = Counter(''.join(arr))
    ag = list(map(lambda p: p[0],filter(lambda kv: kv[1] == len(arr) , counter.items())))
    arr = remove(arr, ag)
    
    # find d among length 3, remove d
    len3 = list(filter(lambda num: len(num) == 3, arr))
    clen3 = Counter(''.join(len3))
    mapping['d'] = list(filter(lambda kv: kv[1] == len(len3), clen3.items()))[0][0]
    arr = remove(arr, [mapping['d']])

    # remove 0 which is the longest str from arr, 7 segments, 2 are a and g
    arr = list(filter(lambda num: len(num)!= 7 - len(mapping) - 2, arr))

    # c3 (c appeared 3 times) e2 f4 b3, found e and f, remove 2 amd 6 which only has e in their length
    counter = Counter(''.join(arr))
    mapping['e'] = list(filter(lambda kv: kv[1] == 2, counter.items()))[0][0]
    mapping['f'] = list(filter(lambda kv: kv[1] == 4, counter.items()))[0][0]

    # the only one left of length 3 is 9, the common segment between 3 and 5 is f
    # remove 2 and 6
    arr = list(filter(lambda num: mapping['e'] not in num and len(num)!=3, arr))

    # remove f
    # distinguish c and b by checking their number of appearance in step 2. 
    arr = remove(arr, [mapping['f']])
    if clen3[arr[0]] == 1:
        mapping['b'], mapping['c'] = arr[0], arr[1]
    else:
        mapping['b'], mapping['c'] = arr[1], arr[0]

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
    reverse = { ''.join(sorted(v)):k for k,v in mapping.items()}
    #print(reverse)
    out = 0
    for f in four:
        if len(f) in easy:
            i = easy[len(f)]
        else:
            decoded = map(lambda c: reverse[c], filter(lambda c: c in reverse, f))
            i = sd[''.join(sorted(decoded))]
        out = out*10 + i
    #print(out)
    total+=out
print(total)
