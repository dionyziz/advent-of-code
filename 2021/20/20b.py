with open('in.txt') as f:
  algo, img = f.read().split('\n\n')

algo = [0 if c == '.' else 1 for c in ''.join(algo.split('\n'))]

board = set()
for y, line in enumerate(img.split('\n')):
  for x, c in enumerate(line):
    if c == '#':
      board.add((x, y))

def enhance(board, baseline):
  output = set()
  xs = set()
  ys = set()

  if algo[0] == 1:
    new_baseline = not baseline

  for x, y in board:
    xs.add(x)
    ys.add(y)

  for x in range(min(xs) - 1, max(xs) + 2):
    for y in range(min(ys) - 1, max(ys) + 2):
      b = ''
      for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
          if ((x + dx, y + dy) in board) != baseline:
            b += '1'
          else:
            b += '0'
      idx = int(b, 2)
      if algo[idx] != new_baseline:
        output.add((x, y))

  return output, new_baseline

baseline = False
for i in range(50):
  board, baseline = enhance(board, baseline)

print(len(board))
