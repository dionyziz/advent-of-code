from parse import parse

with open('input2.txt') as f:
  lines = f.read().splitlines()

valid = 0
for line in lines:
  low, high, letter, password = parse('{:d}-{:d} {:w}: {:w}', line)
  if (password[low - 1] == letter) != (password[high - 1] == letter):
    valid += 1
print(valid)
