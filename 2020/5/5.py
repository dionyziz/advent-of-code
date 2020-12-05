with open('in.txt') as f:
  lines = f.read().splitlines()

def pos(ticket):
  row, col = ticket[:7], ticket[7:]
  row = row.replace('F', '0').replace('B', '1')
  col = col.replace('L', '0').replace('R', '1')

  return int(row, 2), int(col, 2)

def id(row, col):
  return 8 * row + col

rows = set()
cols = set()
ids = set()

for line in lines:
  row, col = pos(line)
  rows.add(row)
  cols.add(col)
  ids.add(id(row, col))

print(max(ids))

for col in cols:
  for row in rows:
    myid = id(row, col)
    if myid not in ids and myid + 1 in ids and myid - 1 in ids:
      print(myid)
