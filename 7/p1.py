PATH = "7/data.txt"

class Color:
    def __init__(self, name):
        self.parents = []
        self.name = name
    def __repr__(self):
        return (self.name + ": {" + str(self.parents) + "}")
def get_all_parents(color):
    res = [x.name for x in colors[color].parents]
    for parent in [x.name for x in colors[color].parents]:
        res += get_all_parents(parent)
    return unique(res)
def unique(li):
    res = []
    for elem in li:
        if not elem in res:
            res.append(elem)
    return res
data = [x[:-1].split(' ') for x in open(PATH)][:-1]
colors = {}
for line in data:
    color1 = ''.join(line[:2])
    if not color1 in colors:
        colors[color1] = Color(color1)
    if line[4] != "no":
        children = (" " + ' '.join(line[4:])).split(',')
        for child in children:
            color2 = ''.join(child.split(' ')[2:4])
            if not color2 in colors:
                colors[color2] = Color(color2)
            colors[color2].parents.append(colors[color1])
print(len(get_all_parents("shinygold")))
