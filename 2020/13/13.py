import math

with open('in.txt') as f:
  timestamp, buses = f.read().splitlines()

timestamp = int(timestamp)
buses = map(int, filter(lambda x: x != 'x', buses.split(',')))
best_time = math.inf
best_bus = None
for bus in buses:
  time = bus - (timestamp % bus)
  if time <= best_time:
    best_bus = bus
    best_time = time
print(best_time * best_bus)
