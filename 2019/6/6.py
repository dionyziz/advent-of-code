from collections import defaultdict

with open('6.txt') as f:
    contents = f.read()

adj = defaultdict(lambda: [])

for line in contents.split("\n"):
    if line != "":
        u, v = line.split(")")
        adj[u].append(v)

def countDescendants(u):
    c = 0
    q = [u]
    while len(q) > 0:
        v = q.pop()
        c += 1
        if v in adj:
            for w in adj[v]:
                q.append(w)

    return c - 1

c = 0
for u in adj:
    c += countDescendants(u)

print(c)
