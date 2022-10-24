PATH = "4/data.txt"
val_ecl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
req = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
def valid(_pass):
    if not all([y in _pass.keys() for y in req]):
        return False
    rules = []
    rules.append(int(_pass["byr"]) >= 1920 and int(_pass["byr"]) <= 2002)
    rules.append(int(_pass["iyr"]) >= 2010 and int(_pass["iyr"]) <= 2020)
    rules.append(int(_pass["eyr"]) >= 2020 and int(_pass["eyr"]) <= 2030)
    hgt_unit = _pass["hgt"][-2:]
    if hgt_unit == "cm" or hgt_unit == "in":
        hgt = int(_pass["hgt"][:-2])
        rules.append((hgt_unit == "cm" and hgt >= 150 and hgt <= 193) or (hgt_unit == "in" and hgt >= 59 and hgt <= 76))
    else:
        rules.append(False)
    rules.append(_pass["hcl"][0] == '#' and all([x in [str(i) for i in range(10)] or x in [chr(i) for i in range(97,103)] for x in _pass["hcl"][1:]]))
    rules.append(_pass["ecl"] in val_ecl)
    rules.append(len(_pass["pid"]) == 9 and all([x in [str(i) for i in range(10)] for x in _pass["pid"]]))
    return all(rules)
dat = [{y.split(':')[0]:y.split(':')[1] for y in x.split(' ')} for x in ''.join(open(PATH).readlines()).translate({ord('
'): ord(' ')}).split("  ")]
print(sum([int(valid(x)) for x in dat])):
