with open('in.txt') as f:
  state = list(map(int, list(f.read().strip())))

MOVES = 100
current = 0
for _ in range(MOVES):
  cur_val = state[current]

  popidx = current + 1
  if popidx >= len(state):
    popidx %= len(state)
    current -= 1
  x = state.pop(popidx)
  popidx = current + 1
  if popidx >= len(state):
    popidx %= len(state)
    current -= 1
  y = state.pop(popidx)
  popidx = current + 1
  if popidx >= len(state):
    popidx %= len(state)
    current -= 1
  z = state.pop(popidx)

  dest = cur_val - 1
  if dest < min(state):
    dest = max(state)
  while dest in (x, y, z):
    dest -= 1
    if dest < min(state):
      dest = max(state)
  dest = state.index(dest)
  state.insert(dest + 1, x)
  state.insert(dest + 2, y)
  state.insert(dest + 3, z)
  if dest < current:
    current += 3
  current = (current + 1) % len(state)

out = ''
idx = state.index(1)
for i, _ in enumerate(state):
  out += str(state[(idx + i + 1) % len(state)])

print(out[:-1])
