# Python code to illustrate split() function
with open("day2/input.txt", "r") as file:
    data = file.readlines()
    y = 0
    x = 0
    a = 0
    d = 0
    for line in data:
        s = line.split(" ")
        v = int(s[1])

        if s[0] == "forward":
            x += v
            d += v * a
        if s[0] == "up":
            y -= v
            a -= v
        if s[0] == "down":
            y += v
            a += v
    print("final depth is ", d*x)