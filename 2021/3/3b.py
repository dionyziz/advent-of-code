from collections import Counter
from itertools import count
from operator import le, gt, itemgetter

with open('in.txt') as f:
  numbers = f.read().splitlines()

def filter_list(pool, coro):
  next(coro)
  while len(pool) > 1:
    predicate = coro.send(pool)
    pool = list(filter(predicate, pool))
  return pool.pop()

def bitfilter_coro(criterion):
  def bitfilter_get_predicate(i, pool):
    ith_bits = map(itemgetter(i), pool)
    bitcounts = Counter(ith_bits)
    desired_bit = str(int(criterion(bitcounts['0'], len(pool) / 2)))
    return lambda item: item[i] == desired_bit
  pool = (yield)
  for i in count():
    pool = (yield bitfilter_get_predicate(i, pool))

oxygen = int(filter_list(numbers, bitfilter_coro(le)), 2)
co2 = int(filter_list(numbers, bitfilter_coro(gt)), 2)

print(oxygen * co2)
