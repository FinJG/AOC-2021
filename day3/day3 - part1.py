one = 0
zero = 0
gamma = []
epsilon = []
with open("input.txt") as i:
    f = i.readlines()
    for loop in range(12):
        for x in f:
            if x[loop] == "1":
                one += 1
            else:
                zero += 1
        if one > zero:
            gamma.append(1)
            epsilon.append(0)
        else:
            gamma.append(0)
            epsilon.append(1)
        one = 0
        zero = 0
print(int("".join([str(i) for i in gamma]),2) * int("".join([str(i) for i in epsilon]),2))

