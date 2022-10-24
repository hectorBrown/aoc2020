PATH = "17/data.txt"
#THIS ONE TAKES AGES
class Hypercube:
    def __init__(self, x, y, z, w):
        self.x = x; self.y = y; self.z = z; self.w = w
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z and self.w == other.w
    def __repr__(self):
        return ("{Hypercube: x=" + str(self.x) + ", y=" + str(self.y) + ", z=" + str(self.z) + ", w=" + str(self.w) + "}")
    def copy(self):
        return Hypercube(self.x, self.y, self.z, self.w)

def count_neighbours4(x,y,z,w,cubes):
    count = 0
    for y_s in range(-1,2):
        for x_s in range(-1,2):
            for z_s in range(-1,2):
                for w_s in range(-1,2):
                    if (y_s or x_s or z_s or w_s):
                        if Hypercube(x + x_s, y + y_s, z + z_s, w + w_s) in hypercubes:
                            count += 1
    return count
data = [x[:-1] for x in open(PATH).readlines()]
hypercubes = []
for y,line in enumerate(data):
    for x,c in enumerate(line):
        if c == '#':
            hypercubes.append(Hypercube(x,y,0,0))
for i in range(6):
    new = [x.copy() for x in hypercubes]
    x_ran = (min([x.x for x in hypercubes]) - 1, max([x.x for x in hypercubes]) + 2)
    y_ran = (min([x.y for x in hypercubes]) - 1, max([x.y for x in hypercubes]) + 2)
    z_ran = (min([x.z for x in hypercubes]) - 1, max([x.z for x in hypercubes]) + 2)
    w_ran = (min([x.w for x in hypercubes]) - 1, max([x.w for x in hypercubes]) + 2)
    for x in range(*x_ran):
        for y in range(*y_ran):
            for z in range(*z_ran):
                for w in range(*w_ran):
                    nei = count_neighbours4(x,y,z,w,cubes)
                    if Hypercube(x,y,z,w) in hypercubes and not (nei == 2 or nei == 3):
                        new.remove(Hypercube(x,y,z,w))
                    elif nei == 3 and not Hypercube(x,y,z,w) in hypercubes:
                        new.append(Hypercube(x,y,z,w))
    hypercubes = [x.copy() for x in new]
    print(str(((i + 1)/6) * 100) + "%")
print(len(hypercubes))
