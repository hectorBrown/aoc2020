PATH = "day16/data.txt"
def valid(rules,prop):
    validity = []
    for rule in rules:
        rulevaliditiy = any([prop >= ran[0] and prop <= ran[1] for ran in rules[rule]])
        validity.append(rulevaliditiy)
    if not any(validity):
        return False
    else:
        return True
data = ''.join(open(PATH)).split("

")
rules = {x.split(':')[0]:[[int(z) for z in y.split('-')] for y in x.split(':')[1].split(" or ")] for x in data[0].split("
")}
my_tick = [int(x) for x in data[1].split('
')[1].split(',')]
near_ticks = [[int(y) for y in x.split(',')] for x in data[2].split('
')[1:-1]]
error_rate = 0
for near_tick in near_ticks:
    for prop in near_tick:
        if not valid(rules, prop):
            error_rate += prop
print(error_rate)
