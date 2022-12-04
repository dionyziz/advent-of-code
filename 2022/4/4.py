with open('in.txt') as f:
  lines = f.read().strip().splitlines()

c = 0
for line in lines:
  a, b = line.split(',')
  la, ra = a.split('-')
  lb, rb = b.split('-')
  la, lb, ra, rb = int(la), int(lb), int(ra), int(rb)
  if la <= lb and rb <= ra\
  or lb <= la and ra <= rb:
    c += 1
print(c)
