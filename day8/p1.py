PATH = "day8/data.txt"

data = [x[:-1].split(' ') for x in open(PATH).readlines()]
acc = 0
i = 0
visited = []
while True:
    command = data[i]
    visited.append(i)
    if command[0] == "acc":
        acc += int(command[1])
        i += 1
    elif command[0] == "jmp":
        i += int(command[1])
    elif command[0] == "nop":
        i += 1
    if i in visited:
        break
print(acc)
