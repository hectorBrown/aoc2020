PATH = "day10/data.txt"

data = [int(x[:-1]) for x in open(PATH).readlines()]
data.sort()
differences = [min(data), 3]
for i,adap in enumerate(data):
    if i != 0:
        differences.append(adap - data[i - 1])
print(len([x for x in differences if x == 1]) * len([x for x in differences if x == 3]))
