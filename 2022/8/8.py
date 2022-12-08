# Dionysis & Joachim

with open('in.txt') as f:
    A = list(f.read().strip().splitlines())

A = [[int(c) for c in line.strip()] for line in A]
T = list(zip(*A))

cnt = 0
for y, row in enumerate(A):
    for x, c in enumerate(row):
        views = [A[y][:x][::-1], A[y][x + 1:], T[x][:y][::-1], T[x][y + 1:]]
        cnt += any(all(tree < c for tree in view) for view in views)
print(cnt)