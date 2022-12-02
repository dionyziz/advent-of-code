with open('in.txt') as f:
  backpacks = [
    [int(food) for food in elf.split('\n')]
    for elf in f.read().strip().split('\n\n')
  ]

print(sum(sorted([sum(foods) for foods in backpacks])[-3:]))
