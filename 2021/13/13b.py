with open('in.txt') as f:
  dots, instructions = f.read().split('\n\n')

dots = dots.split('\n')
instructions = instructions.split('\n')[:-1]

board = set()
for dot in dots:
  board.add(map(int, dot.split(',')))

def print_board(board):
  max_x = max([x for x, y in board])
  max_y = max([y for x, y in board])

  for y in range(max_y + 1):
    for x in range(max_x + 1):
      if (x, y) in board:
        print('#', end='')
      else:
        print('.', end='')
    print()
  print()

for instruction in instructions:
  instruction = instruction.split('fold along ')[1]
  direction, location = instruction.split('=')
  direction = { 'x': 0, 'y': 1 }[direction]
  location = int(location)

  new_board = set()
  for dot in board:
    dot = list(dot)
    if dot[direction] > location:
      dot[direction] = 2*location - dot[direction]
    new_board.add(tuple(dot))
  board = new_board

print_board(board)
