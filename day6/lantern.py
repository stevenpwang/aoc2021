with open("day6/input.txt", "r") as file:
    data = file.readlines()
arr = data[0].split(",")
counter = [0]*9
for i in arr:
    counter[int(i)] +=1
print(counter)
for d in range(256):
    print(d)
    new_fish = counter[0]
    counter = counter[1:]
    counter[6] += new_fish
    counter.append(new_fish)
print(sum(counter))