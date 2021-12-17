x1, y1 = 138, -125
x2, y2 = 184, -71

def simulate(vx, vy):
  x, y = 0, 0
  while True:
    if x > x2 or y < y1:
      return False
    if x1 <= x and y <= y2:
      return True
    x += vx
    y += vy
    if vx > 0:
      vx -= 1
    vy -= 1

print(len([1 for vx in range(1, x2 + 1) for vy in range(-1000, 1000) if simulate(vx, vy)]))
