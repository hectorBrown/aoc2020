PATH = "17/data.txt"
class Cube:
    def __init__(self, x, y, z):
        self.x = x; self.y = y; self.z = z
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z
    def __repr__(self):
        return ("{Cube: x=" + str(self.x) + ", y=" + str(self.y) + ", z=" + str(self.z) + "}")
    def copy(self):
        return Cube(self.x, self.y, self.z)
def count_neighbours(x,y,z,cubes):
    count = 0
    for y_s in range(-1,2):
        for x_s in range(-1,2):
            for z_s in range(-1,2):
                if (y_s or x_s or z_s):
                    if Cube(x + x_s, y + y_s, z + z_s) in cubes:
                        count += 1
    return count
def map(z, cubes):
    new = [x for x in cubes if x.z == z]
    if len(new):
        x_ran = (min([x.x for x in new]) - 1, max([x.x for x in new]) + 2)
        y_ran = (min([x.y for x in new]) - 1, max([x.y for x in new]) + 2)
        print("z=" + str(z))
        print("x_min=" + str(x_ran[0]))
        print("y_min=" + str(y_ran[0]))
        for y in range(*y_ran):
            s = ""
            for x in range(*x_ran):
                if Cube(x,y,z) in new:
                    s += "#"
                else:
                    s += '.'
            print(s)
data = [x[:-1] for x in open(PATH).readlines()]
cubes = []
for y,line in enumerate(data):
    for x,c in enumerate(line):
        if c == '#':
            cubes.append(Cube(x,y,0))
for i in range(6):
    new = [x.copy() for x in cubes]
    x_ran = (min([x.x for x in cubes]) - 1, max([x.x for x in cubes]) + 2)
    y_ran = (min([x.y for x in cubes]) - 1, max([x.y for x in cubes]) + 2)
    z_ran = (min([x.z for x in cubes]) - 1, max([x.z for x in cubes]) + 2)
    for x in range(*x_ran):
        for y in range(*y_ran):
            for z in range(*z_ran):
                nei = count_neighbours(x,y,z,cubes)
                if Cube(x,y,z) in cubes and not (nei == 2 or nei == 3):
                    new.remove(Cube(x,y,z))
                elif nei == 3 and not Cube(x,y,z) in cubes:
                    new.append(Cube(x,y,z))
    cubes = [x.copy() for x in new]
print(len(cubes))
