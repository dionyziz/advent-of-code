from collections import Counter

with open('in.txt') as f:
  numbers = f.read().splitlines()

transposed = zip(*numbers)

bitcounts = map(Counter, transposed)
gammabits = [x.most_common(1)[0][0] for x in bitcounts]
epsilonbits = ['0' if x == '1' else '1' for x in gammabits]

gamma = int(''.join(gammabits), 2)
epsilon = int(''.join(epsilonbits), 2)

print(gamma * epsilon)
