from pygame.math import Vector2

with open('in.txt') as f:
  lines = f.read().splitlines()

location = Vector2(0, 0)
waypoint = Vector2(10, -1)
for line in lines:
  instruction, amount = line[0], int(line[1:])
  cardinals = {
    'E': (1, 0),
    'W': (-1, 0),
    'N': (0, -1),
    'S': (0, 1)
  }
  if instruction in cardinals:
    delta = Vector2(cardinals[instruction])
    waypoint += amount * delta
  elif instruction == 'F':
    location += amount * waypoint
  elif instruction == 'L':
    waypoint.rotate_ip(-amount)
  elif instruction == 'R':
    waypoint.rotate_ip(amount)

print(sum(map(abs, location)))
