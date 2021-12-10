PATH = "day10/data.txt"
class Adapter:
    def __init__(self, value):
        self.parents = []
        self.val = value
        self.routes = 1
data = [int(x[:-1]) for x in open(PATH).readlines()]
data.sort()
adapters = {0: Adapter(0)}
routes = {0: 0}
for value in data:
    adapters[value] = Adapter(value)
    for i in range(value - 3, value):
        if i in adapters:
            adapters[value].parents.append(adapters[i])
    adapters[value].routes = sum([parent.routes for parent in adapters[value].parents])
print(adapters[data[-1]].routes)
