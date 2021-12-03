from collections import Counter

with open('in.txt') as f:
  numbers = f.read().splitlines()

transposed = zip(*numbers)

bitcounts = map(Counter, transposed)
gammabits = list(map(lambda x: x.most_common(1)[0][0], bitcounts))
epsilonbits = map(lambda x: '0' if x == '1' else '1', gammabits)

gamma = int(''.join(gammabits), 2)
epsilon = int(''.join(epsilonbits), 2)

print(gamma * epsilon)
