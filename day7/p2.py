PATH = "day7/data.txt"
class Color:
    def __init__(self, name):
        self.children = {}
        self.name = name
    def __repr__(self):
        return (self.name + ": {" + str(self.children) + "}")
def no_of_children(color):
    no = 1
    for child in colors[color].children:
        no += colors[color].children[child] * no_of_children(child.name)
    return no
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
            colors[color1].children[colors[color2]] = int(child.split(' ')[1])
print(no_of_children("shinygold") - 1)
