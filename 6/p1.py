PATH = "6/data.txt"


data = ''.join(open(PATH).readlines()).translate({ord('
'): ord(' ')})[:-1].split("  ")
count = 0
for group in data:
    answered = []
    for person in group.split(' '):
        for question in person:
            if not question in answered:
                answered.append(question)
                count += 1
print(count)
