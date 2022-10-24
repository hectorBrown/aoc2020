PATH = "15/data.txt"
dat = [int(x) for x in open(PATH).readline()[:-1].split(',')]
target = 30000000
spoken = {}
for i,term in enumerate(dat[:-1]):
    spoken[term] = i
last = dat[-1]
for i in range(len(dat) - 1, target - 1):
    curr = 0
    if not last in spoken:
        curr = 0
    else:
        curr = i - spoken[last]
    spoken[last] = i
    last = curr
print(last)
