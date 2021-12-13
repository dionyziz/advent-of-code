with open('in.txt') as f:
  dots, instructions = f.read().split('\n\n')

dots = dots.split('\n')
instructions = instructions.split('\n')[:-1]

board = set()
for dot in dots:
  board.add(map(int, dot.split(','))

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
  break

print(len(new_board))
