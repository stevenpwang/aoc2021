def findzs(data):
    zero = list()
    for line in data:
        if len(zero) ==0:
            zero =  [0]* len(line)
        for idx, c in enumerate(list(line)):
            if c == '0':
                zero[idx] += 1
    zero = zero[:-1]
    return zero

def ztos(zero, total):
    s = ""
    for i in zero:
        if i > total/2:
            s+='0'
        else:
            s+='1'
    return s

def filterz(data):
    filtered = list()
    co2 = data
    i = 0
    while len(co2)!=1:
        print("len co2 is ",len(co2))
        zs = findzs(co2)
        s = ztos(zs, len(co2))
        print("zs is ",zs)
        print("s is ",s)

        for line in co2:
            if line[i] != s[i]:  # change this between == and != to get co2 and ox
                filtered.append(line)
        i+=1
        co2 = filtered
        filtered = list()

    print("co2 ", co2)

zero = list()
total = 0
data = ""
with open("day3/input.txt", "r") as file:
    data = file.readlines()
    total = len(data)
    zero = findzs(data)
print("zeros is ", zero, total)

gamma = 0
epilson = 0
for i in zero:
    gamma = gamma * 2
    epilson = epilson *2
    if i > total/2:
        gamma +=1
    else:
        epilson +=1
print("gamma, epilson ", gamma, epilson)
print("power ", gamma*epilson)

filterz(data)