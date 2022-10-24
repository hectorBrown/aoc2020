PATH = "4/data.txt"
req = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
dat = [{y.split(':')[0]:y.split(':')[1] for y in x.split(' ')} for x in ''.join(open(PATH).readlines()).translate({ord('
'): ord(' ')}).split("  ")]
print(sum([int(all([y in x.keys() for y in req])) for x in dat]))
