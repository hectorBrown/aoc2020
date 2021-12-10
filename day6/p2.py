PATH = "day6/data.txt"
data = ''.join(open(PATH).readlines()).translate({ord('
'): ord(' ')})[:-1].split("  ")
count = 0
for group in data:
    answered = []
    for person in group.split(' '):
        answered.append(list(person))
    count += len([x for x in answered[0] if all([x in y for y in answered[1:]])])
print(count)
