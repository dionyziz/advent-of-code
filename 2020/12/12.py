from pygame.math import Vector2

with open('in.txt') as f:
  lines = f.read().splitlines()

location = Vector2(0, 0)
direction = Vector2(1, 0)
for line in lines:
  instruction, amount = line[0], int(line[1:])
  cardinals = {
    'E': (1, 0),
    'W': (-1, 0),
    'N': (0, -1),
    'S': (0, 1),
    'F': direction
  }
  if instruction in cardinals:
    delta = Vector2(cardinals[line[0]])
    location += amount * delta
  if instruction == 'L':
    direction.rotate_ip(-amount)
  elif instruction == 'R':
    direction.rotate_ip(amount)

print(sum(map(abs, location)))
