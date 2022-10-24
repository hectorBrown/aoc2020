PATH = "8/data.txt"
def valid(commands):
    i = 0
    acc = 0
    visited = []
    while True:
        command = commands[i]
        visited.append(i)
        if command[0] == "acc":
            acc += int(command[1])
            i += 1
        elif command[0] == "jmp":
            i += int(command[1])
        elif command[0] == "nop":
            i += 1
        if i in visited:
            return False
        elif i == len(commands) - 1:
            return True
def getacc(commands):
    i = 0
    acc = 0
    while True:
        command = commands[i]
        if command[0] == "acc":
            acc += int(command[1])
            i += 1
        elif command[0] == "jmp":
            i += int(command[1])
        elif command[0] == "nop":
            i += 1
        if i == len(commands):
            break
    return acc
    
data = [x[:-1].split(' ') for x in open(PATH).readlines()]
for i,command in enumerate(data):
    if command[0] == "nop" or command[0] == "jmp":
        new = data.copy()
        new[i] = data[i].copy()
        new[i][0] = "jmp" if command[0] == "nop" else "nop"
        if valid(new):
            print(getacc(new))
    
