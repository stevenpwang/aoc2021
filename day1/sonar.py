# Python code to illustrate split() function
with open("day1/input.txt", "r") as file:
    data = file.readlines()
    prev = ""
    inc = 0
    for line in data:
        print(line)
        if prev != "":
            p = int(prev)
            l = int(line)
            if l > p:
                inc +=1
        prev = line
    print("inc is ", inc)