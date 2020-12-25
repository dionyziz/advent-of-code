with open('in.txt') as f:
  pub = list(map(int, f.read().splitlines()))

MOD = 20201227
GENERATOR = 7

def pub2priv(pub):
  prod = 1
  for priv in range(0, MOD):
    if prod == pub:
      return priv
    prod *= GENERATOR
    prod %= MOD
  return None

priv0 = pub2priv(pub[0])
print(pow(pub[1], priv0, MOD))
