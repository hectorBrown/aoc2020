PATH = "day5/data.txt"
dat = [x[:-1] for x in open(PATH).readlines()][:-1]
ids = []
for seat in dat:
    row_ran = 128
    lowest_row = 0
    col_ran = 8
    lowest_col = 0
    for c in seat[:-3]:
        if c == 'B':
            lowest_row += row_ran / 2
        row_ran /= 2
    for c in seat[-3:]:
        if c == 'R':
            lowest_col += col_ran / 2
        col_ran /= 2
    ids.append(lowest_row * 8 + lowest_col)
ids.sort()
for i, idn in enumerate(ids):
    if ids[i + 1] != idn + 1:
        print(idn + 1)
        break
