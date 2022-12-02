with open('in.txt') as f:
  backpacks = [
    [int(food) for food in elf.split('\n')]
    for elf in f.read().strip().split('\n\n')
  ]

print(max([sum(foods) for foods in backpacks]))
