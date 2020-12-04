from parse import parse
from collections import Counter

with open('input.txt') as f:
  lines = f.read().splitlines()

valid = 0
for line in lines:
  low, high, letter, password = parse('{:d}-{:d} {:w}: {:w}', line)
  counter = Counter(password)
  if low <= counter[letter] <= high:
    valid += 1
print(valid)
