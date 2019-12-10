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

def angle(num):
    num *= np.exp(np.pi / 2 * 1j)
    return round(np.angle(num), ERROR) % (2 * np.pi)

best_count = 0
for candidate_station in asteroids:
    angles = set()
    for optical_target in asteroids.difference([candidate_station]):
        angles.add(angle(optical_target - candidate_station))
    if len(angles) > best_count:
        best_count = len(angles)
        station = candidate_station

field_of_view = defaultdict(lambda: [])
asteroids.remove(station)
for optical_target in asteroids:
    num = optical_target - station
    heappush(field_of_view[angle(num)], (np.absolute(num), optical_target))

destroyed = []
survivors = asteroids
destruction_path = sorted(field_of_view.items())

while len(survivors):
    for angle, beam in destruction_path:
        if len(beam):
            _, victim = heappop(beam)
            destroyed.append(victim)
            survivors.remove(victim)

print(100 * destroyed[199].real + destroyed[199].imag)
