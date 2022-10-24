PATH = "1/data.txt"
f = open(PATH)
dat = [int(x[:-1]) for x in f.readlines()]
for i,x in enumerate(dat):
    others = dat.copy()
    others.pop(i)
    for j,y in enumerate(others):
        others_2 = others.copy()
        others_2.pop(j)
        for k,z in enumerate(others_2):
            if x + y + z == 2020:
                print(x*y*z)
