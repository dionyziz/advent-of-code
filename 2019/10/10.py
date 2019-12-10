import numpy as np
from heapq import heappush, heappop
from collections import defaultdict

ERROR = 10
EPSILON = 10**(-ERROR)

with open('10.txt') as f:
    rows = f.read().split('\n')[:-1]

asteroids = set()
for y, row in enumerate(rows):
    for x, marker in enumerate(row):
        if marker == '#':
            asteroids.add(x + y * 1j)

best_count = 0
for candidate_station in asteroids:
    field_of_view = defaultdict(lambda: [])
    for optical_target in asteroids.difference([candidate_station]):
        num = optical_target - candidate_station
        angle = round(np.angle(num * 1j), ERROR) % (2 * np.pi)
        heappush(field_of_view[angle], (np.absolute(num), optical_target))
    if len(field_of_view) > best_count:
        best_count = len(field_of_view)
        best_field_of_view = field_of_view
        station = candidate_station

destroyed = []
survivors = asteroids.difference([station])
destruction_path = sorted(best_field_of_view.items())

while len(survivors):
    for angle, beam in destruction_path:
        if len(beam):
            _, victim = heappop(beam)
            destroyed.append(victim)
            survivors.remove(victim)

print(100 * destroyed[199].real + destroyed[199].imag)
