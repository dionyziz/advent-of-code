# Dionysis & Joachim

with open('in.txt') as f:
    A = list(f.read().strip().splitlines())

A = [[int(c) for c in line.strip()] for line in A]
T = list(zip(*A))

best = 0
for y, row in enumerate(A):
    for x, tree in enumerate(row):
        views = [A[y][:x][::-1], A[y][x + 1:], T[x][:y][::-1], T[x][y + 1:]]
        score = 1
        for view in views:
            try:
                score *= list(v >= tree for v in view).index(True) + 1
            except ValueError:
                score *= len(view)
        best = max(score, best)
print(best)