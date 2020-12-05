import re

with open('in.txt') as f:
  input = f.read().split('\n\n')

rules = {
  'byr': lambda x: 1920 <= int(x) <= 2002,
  'iyr': lambda x: 2010 <= int(x) <= 2020,
  'eyr': lambda x: 2020 <= int(x) <= 2030,
  'hgt': lambda x: x[-2:] == 'cm' and 150 <= int(x[:-2]) <= 193 or\
                   x[-2:] == 'in' and 59 <= int(x[:-2]) <= 76,
  'hcl': lambda x: re.match(r'^\#[0-9a-f]{6}$', x),
  'ecl': lambda x: x in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'),
  'pid': lambda x: re.match(r'^[0-9]{9}$', x)
}

def valid(passport):
  for key in rules:
    if key not in passport or not rules[key](passport[key]):
      return False
  return True

count = 0
for data in input:
  fields = data.split()
  passport = {}
  for field in fields:
    key, value = field.split(':')
    passport[key] = value
  count += valid(passport)

print(count)
