with open('in.txt') as f:
  lines = f.read().splitlines()

patterns = [
  'abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf',
  'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg'
]

cnt = 0
for line in lines:
  probe, value = line.split(' | ')
  for word in value.split(' '):
    if len(word) in (2, 4, 3, 7):
      cnt += 1

print(cnt)
