from parse import parse
import numpy as np
from math import isclose

with open('in.txt') as f:
  machines = f.read().split('\n\n')

OFFSET = 10000000000000
REL_TOL = 1e-15
sum = 0
for i, machine in enumerate(machines):
  Ax, Ay, Bx, By, Cx, Cy = parse("Button A: X+{:d}, Y+{:d}\nButton B: X+{:d}, Y+{:d}\nPrize: X={:d}, Y={:d}", machine)
  Cx += OFFSET
  Cy += OFFSET
  A = np.array([[Ax, Bx], [Ay, By]])
  B = np.array([Cx, Cy])
  try:
    C = np.linalg.solve(A, B)
  except np.linalg.LinAlgError:
    continue
  if isclose(C[0], round(C[0]), rel_tol=REL_TOL) and isclose(C[1], round(C[1]), rel_tol=REL_TOL):
    sum += round(3 * C[0] + C[1])
print(sum)