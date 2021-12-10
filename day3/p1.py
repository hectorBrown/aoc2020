PATH = "day3/data.txt"

f = open(PATH)
dat = f.readlines()
_map = [list(x[:-1]) for x in dat]
pos = [0,0]
counter = 0
while pos[0] < len(_map):
    if _map[pos[0]][pos[1]] == '#':
        counter += 1
    pos[0] += 1
    pos[1] += 3
    if pos[1] >= len(_map[0]):
        pos[1] -= len(_map[0])
print(counter)
