PATH = "15/data.txt"
def get_next(history):
    temp = history.copy()
    temp.reverse()
    if temp[0] in temp[1:]:
        return temp[1:].index(temp[0]) + 1
    else:
        return 0
dat = [int(x) for x in open(PATH).readline()[:-1].split(',')]
target = 2020
for i in range(target - len(dat)):
    dat.append(get_next(dat))
print(dat[-1])
