with open('in.txt') as f:
  instructions = f.read().splitlines()

location = 0
for instruction in instructions:
  direction, amount = instruction.split(' ')
  amount = int(amount)
  location += amount * {
    'forward': 1,
    'down': 1j,
    'up': -1j
  }[direction]

print(int(location.real * location.imag))
