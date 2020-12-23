from collections import deque
from itertools import count

with open('in.txt') as f:
  players = f.read().split('\n\n')

players[0] = players[0].splitlines()[1:]
players[1] = players[1].splitlines()[1:]
players[0] = deque(map(int, players[0]))
players[1] = deque(map(int, players[1]))

memo = {}

def game(players):
  conf = (tuple(players[0]), tuple(players[1]))
  try:
    return memo[conf]
  except:
    pass

  seen = set()

  while players[0] and players[1]:
    prev = (tuple(players[0]), tuple(players[1]))
    if prev in seen:
      memo[conf] = 0
      return 0
    seen.add(prev)
    move(players)

  if players[0]:
    memo[conf] = 0
    return 0
  memo[conf] = 1
  return 1

def move(players):
  cards = players[0].popleft(), players[1].popleft()
  if cards[0] <= len(players[0]) and cards[1] <= len(players[1]):
    # recurse
    winner = game([
      deque(list(players[0])[:cards[0]]),
      deque(list(players[1])[:cards[1]])
    ])
  else:
    if cards[0] > cards[1]:
      winner = 0
    else:
      winner = 1
  players[winner].append(cards[winner])
  players[winner].append(cards[1 - winner])
  return winner

def score(player):
  return sum(x * y for x, y in zip(count(1), list(player)[::-1]))

winner = game(players)
print('winner:', winner)
print(score(players[winner]))
