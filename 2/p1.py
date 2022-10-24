PATH = "2/data.txt"


def valid(l):
    char = l[0][-1:]
    passw = l[1][1:]
    _range = [int(x) for x in l[0][:-1].split('-')]
    return passw.count(char) >= _range[0] and passw.count(char) <= _range[1]

f = open(PATH)
dat = [x[:-1].split(':') for x in f.readlines()]
print(len(list(filter(valid, dat))))
