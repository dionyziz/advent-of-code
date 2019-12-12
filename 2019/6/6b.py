with open('6.txt') as f:
    contents = f.read()

adj = {}

for line in contents.split("\n"):
    if line != "":
        u, v = line.split(")")
        if u not in adj:
            adj[u] = []
        if v not in adj:
            adj[v] = []
        adj[u].append(v)
        adj[v].append(u)

def bfs(s, t):
    visited = {}
    q = [(s, 0)]
    while len(q) > 0:
        v, c = q.pop()
        visited[v] = True
        if v == t:
            return c
        if v in adj:
            for w in adj[v]:
                if w not in visited:
                    q.append((w, c + 1))
    return -1

print(bfs("YOU", "SAN") - 2)
