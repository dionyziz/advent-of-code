from collections import defaultdict

with open('6.txt') as f:
    contents = f.read()

adj = defaultdict(lambda: set())

for line in contents.split("\n"):
    if line != "":
        u, v = line.split(")")
        adj[u].add(v)
        adj[v].add(u)

def bfs(s, t):
    visited = set()
    q = [(s, 0)]
    while len(q) > 0:
        v, c = q.pop()
        visited.add(v)
        if v == t:
            return c
        for w in adj[v].difference(visited):
            q.append((w, c + 1))

print(bfs("YOU", "SAN") - 2)
