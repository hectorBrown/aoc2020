PATH = "13/data.txt"

f = open(PATH)
depart = int(f.readline())
buses = [int(elem) for elem in f.readline().split(',') if not elem == 'x']
f.close()
curr = depart
while all([curr % bus for bus in buses]):
    curr += 1
print((curr - depart) * [bus for bus in buses if curr % bus == 0][0])
