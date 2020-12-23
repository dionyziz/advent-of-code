from collections import deque
from itertools import count

with open('in.txt') as f:
  players = f.read().split('\n\n')

players[0] = players[0].splitlines()[1:]
players[1] = players[1].splitlines()[1:]
players[0] = deque(map(int, players[0]))
players[1] = deque(map(int, players[1]))

def move(players):
  cards = players[0].popleft(), players[1].popleft()
  if cards[0] > cards[1]:
    winner = 0
  else:
    winner = 1
  players[winner].append(cards[winner])
  players[winner].append(cards[1 - winner])

while players[0] and players[1]:
  move(players)

def score(player):
  return sum(x * y for x, y in zip(count(1), list(player)[::-1]))

if players[0]:
  winner = 1
else:
  winner = 0
print('winner:', winner)
print(sum(map(score, players)))
