
def num1():
    one = 0
    zero = 0
    with open("input.txt") as i:
        f = i.readlines()
        for loop in range(12):
            for i in f:
                if i[loop] == "1":
                    one += 1
                else:
                    zero += 1
            if one >= zero:
                f = [i for i in f if i[loop] == "1"]
            else:
                f = [i for i in f if i[loop] == "0"]
            one = 0
            zero = 0
    return f

def num2():
    one = 0
    zero = 0
    with open("input.txt") as i:
        f = i.readlines()
        for loop in range(9):
            for i in f:
                if i[loop] == "1":
                    one += 1
                else:
                    zero += 1
            if one >= zero:
                f = [i for i in f if i[loop] == "0"]
            else:
                f = [i for i in f if i[loop] == "1"]
            one = 0
            zero = 0
    return f

print(int(num2()[0], 2) * int(num1()[0],2))