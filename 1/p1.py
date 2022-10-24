PATH = "1/data.txt"

f = open(PATH)
dat = [int(x[:-1]) for x in f.readlines()]
for i,x in enumerate(dat[:-1]):
    for y in dat[i + 1:]:
        if x + y == 2020:
            print(x*y)

