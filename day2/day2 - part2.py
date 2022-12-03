horizontal = 0
depth = 0
aim = 0
with open("input.txt") as i:
    for loop in [i[:-1] for i in i.readlines()]:
        splt = loop.split(" ")
        if splt[0] == "up":
            aim -= int(splt[1])
        if splt[0] == "down":
            aim += int(splt[1])
        if splt[0] == "forward":
            horizontal += int(splt[1])
            depth += int(splt[1]) * aim
print(horizontal * depth)



