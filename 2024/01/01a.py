with open('in.txt') as f:
  lines = f.readlines()

lines = [(int(num) for num in pair.split()) for pair in lines]
lists = map(sorted, zip(*lines))
diffs = [abs(b - a) for a, b in zip(*lists)]

print(sum(diffs))
