PATH = "day14/data.txt"
def assign(add, mask, mem, val):
    val = list(val)
    for i,c in enumerate(mask):
        if c != 'X':
            val[i] = c
    mem[add] = decimal(''.join(val))
def binary(val):
    res = ""
    for i in range(35, -1, -1):
        if val >= 2**i:
            res += "1"
            val -= 2**i
        else:
            res += "0"
    return res
def decimal(val):
    val = list(val)
    val.reverse()
    val = ''.join(val)
    res = 0
    for i,c in enumerate(val):
        if c == '1':
            res += 2**i
    return res
data = [x[:-1].split(" = ") for x in open(PATH).readlines()]
mask = ""
mem = {}
for command in data:
    if  command[0] == "mask":
        mask = command[1]
    else:
        assign(int(command[0][4:-1]),mask,mem,binary(int(command[1])))
print(sum([mem[key] for key in mem]))
