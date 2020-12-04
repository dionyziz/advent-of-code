with open('in.txt') as f:
  lines = f.read().splitlines()

def trees(slope_y, slope_x):
  trees = 0
  x = 0
  for y in range(0, len(lines), slope_x):
    line = lines[y]
    trees += line[x % len(line)] == '#'
    x += slope_y
  return trees

print(trees(3, 1))

p = 1
for slope_y, slope_x in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2)):
  p *= trees(slope_y, slope_x)
print(p)
