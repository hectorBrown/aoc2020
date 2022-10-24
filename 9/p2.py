PATH = "9/data.txt"
def get_all_combos(li):
    res = []
    for i,elem1 in enumerate(li):
        li2 = li.copy()
        li2.pop(i)
        for elem2 in li2:
            res.append(elem1 + elem2)
    return res


preamble = 25
broken = 0
data = [int(x) for x in open(PATH).readlines()]
for i in range(preamble, len(data)):
    _range = data[i - preamble:i]
    if not data[i] in get_all_combos(_range):
        broken = data[i]
found = False
base = 0
length = 1
while not found:
    res = sum(data[base:base + length])
    found = res == broken
    if found:
        print(min(data[base:base + length]) + max(data[base:base + length]))
    elif res > broken:
        length = 1
        base += 1
    else:
        length += 1
        
