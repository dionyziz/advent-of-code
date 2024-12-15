from parse import parse
import numpy as np
from math import isclose

with open('in.txt') as f:
  machines = f.read().split('\n\n')

sum = 0
for machine in machines:
  Ax, Ay, Bx, By, Cx, Cy = parse("Button A: X+{:d}, Y+{:d}\nButton B: X+{:d}, Y+{:d}\nPrize: X={:d}, Y={:d}", machine)
  A = np.array([[Ax, Bx], [Ay, By]])
  B = np.array([Cx, Cy])
  try:
    C = np.linalg.solve(A, B)
  except np.linalg.LinAlgError:
    continue
  if isclose(C[0], round(C[0])) and isclose(C[1], round(C[1])):
    sum += round(3 * C[0] + C[1])
print(sum)