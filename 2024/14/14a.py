from parse import parse
from math import prod

with open('in.txt') as f:
  lines = f.read().splitlines()

ITERATIONS = 100
MAX_X = 101
MAX_Y = 103

pos = []
vel = []
for line in lines:
  px, py, vx, vy = parse("p={:d},{:d} v={:d},{:d}", line)
  pos.append([px, py])
  vel.append([vx, vy])

for _ in range(ITERATIONS):
  for i in range(len(pos)):
    pos[i][0] += vel[i][0]
    pos[i][0] %= MAX_X
    pos[i][1] += vel[i][1]
    pos[i][1] %= MAX_Y

quads = [0] * 4
for pt in pos:
  if pt[0] < MAX_X // 2 and pt[1] < MAX_Y // 2:
    quads[0] += 1
  elif pt[0] < MAX_X // 2 and pt[1] > MAX_Y // 2:
    quads[1] += 1
  elif pt[0] > MAX_X // 2 and pt[1] < MAX_Y // 2:
    quads[2] += 1
  elif pt[0] > MAX_X // 2 and pt[1] > MAX_Y // 2:
    quads[3] += 1

print(prod(quads))