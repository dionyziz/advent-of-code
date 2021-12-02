with open('small.txt') as f:
  instructions = f.read().splitlines()

location = 0
aim = 0
for instruction in instructions:
  direction, amount = instruction.split(' ')
  amount = int(amount)
  if direction == 'down':
    aim += amount
  elif direction == 'up':
    aim -= amount
  else:
    location += amount + aim * amount * 1j

print(int(location.real * location.imag))
