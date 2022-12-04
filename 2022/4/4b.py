with open('in.txt') as f:
  lines = f.read().strip().splitlines()

c = 0
for line in lines:
  a, b = line.split(',')
  la, ra = a.split('-')
  lb, rb = b.split('-')
  la, lb, ra, rb = int(la), int(lb), int(ra), int(rb)
  if la <= lb and lb <= ra\
  or lb <= la and la <= rb:
    c += 1
print(c)
