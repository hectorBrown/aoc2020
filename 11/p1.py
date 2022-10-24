PATH = "11/data.txt"

def count_occ(mat, i, j):
    count = 0
    for i_s in range(-1, 2):
        for j_s in range(-1, 2):
            if (i_s or j_s) and i_s + i >= 0 and i_s + i < len(mat) and j_s + j >= 0 and j_s + j < len(mat[0]):
                if mat[i + i_s][j + j_s] == '#':
                    count += 1
    return count
data = [list(x[:-1]) for x in open(PATH).readlines()]
changed = True
while changed:
    changed = False
    new = [line.copy() for line in data]
    for i,row in enumerate(data):
        for j,c in enumerate(row):
            if c == 'L' and not count_occ(data, i, j):
                new[i][j] = '#'
                changed = True
            elif c == '#' and count_occ(data, i, j) >= 4:
                new[i][j] = 'L'
                changed = True
    data = [line.copy() for line in new]
print(sum([len([elem for elem in line if elem == '#']) for line in data]))
