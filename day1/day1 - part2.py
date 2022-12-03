count = 0
with open("input.txt") as i:
    f = [int(i[:-1]) for i in i.readlines()]
    f = [sum(f[i:i+3]) for i,v in enumerate(f)]
    save = 0
    for i in f:
        if save < i:
            count += 1
        save = i
print(count-1)
