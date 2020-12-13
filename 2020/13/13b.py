from sympy.ntheory.modular import crt

with open('in.txt') as f:
  _, buses = f.read().splitlines()

moduli = []
residues = []
for i, bus in enumerate(buses.split(',')):
  if bus != 'x':
    bus = int(bus)
    moduli.append(bus)
    residues.append(bus - i)

print(crt(moduli, residues)[0])
