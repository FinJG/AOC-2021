forward = 0
down = 0
up = 0
with open("input.txt") as i:
    for loop in [i[:-1] for i in i.readlines()]:
        splt = loop.split(" ")
        locals()[splt[0]] += int(splt[1])
print(forward * (down-up))