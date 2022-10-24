PATH = "12/data.txt"
def run(command, pos, way):
    if command[0] == 'N':
        way[1] += command[1]
    elif command[0] == 'E':
        way[0] += command[1]
    elif command[0] == 'W':
        way[0] -= command[1]
    elif command[0] == 'S':
        way[1] -= command[1]
    elif command[0] == 'L':
        way = rotate_way(int(command[1]/90), way)
    elif command[0] == 'R':
        way = rotate_way(int((360- command[1])/90), way)
    else:
        for i in range(command[1]):
            pos[0] += way[0]
            pos[1] += way[1]
    return [pos, way]
def rotate_way(step, way):
    for i in range(step):
        way[0],way[1] = -way[1],way[0]
    return way
data = [[x[:-1][0], int(x[:-1][1:])] for x in open(PATH).readlines()]
pos = [0,0]
way = [10,1]
for command in data:
    pos, way = run(command, pos, way)
print(abs(pos[0]) + abs(pos[1]))
