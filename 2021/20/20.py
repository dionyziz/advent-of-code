with open('in.txt') as f:
  algo, img = f.read().split('\n\n')

board = set()
for y, line in enumerate(img.split('\n')):
  for x, c in enumerate(line):
    if c == '#':
      board.add((x, y))

def enhance(board):
  output = set()
  xs = set()
  ys = set()

  for x, y in board:
    xs.add(x)
    ys.add(y)

  for x in range(min(xs) - 1, max(xs) + 2):
    for y in range(min(ys) - 1, max(ys) + 2):
      b = ''
      for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
          if (x + dx, y + dy) in board:
            b += '1'
          else:
            b += '0'
      idx = int(b, 2)
      if algo[idx] == '#':
        output.add((x, y))

  return output

print(len(board))
