import re
import numpy as np

with open("12.txt") as f:
    contents = f.readlines()

class Moon:
    def __init__(self, position):
        self.position = position
        self.velocity = np.array([0, 0, 0])

    def energy(self):
        pot = np.sum(np.abs(self.position))
        kin = np.sum(np.abs(self.velocity))

        return pot*kin

    def __repr__(self):
        return 'pos=<x=' + \
               str(self.position[0]) + ', y=' + \
               str(self.position[1]) + ', z=' + \
               str(self.position[2]) + '>, vel=<x=' + \
               str(self.velocity[0]) + ', y=' + \
               str(self.velocity[1]) + ', z=' + \
               str(self.velocity[2]) + '>'

moons = []
for line in contents:
    match = re.match(r".*=([-0-9]+).*=([-0-9]+).*=([-0-9]+)", line)
    position = np.array(list(map(int, match.groups())))
    moons.append(Moon(position))

TARGET_STEP = 1000

step = 0
snapshots = [set(), set(), set()]
repeat = [None, None, None]
while True:
    for dimension in range(3):
        if repeat[dimension] is not None:
            continue
        snapshot = []
        for moon in moons:
            snapshot.append((moon.position[dimension], moon.velocity[dimension]))
        snapshot = tuple(snapshot)
        if snapshot in snapshots[dimension]:
            repeat[dimension] = step
        snapshots[dimension].add(snapshot)
    if all(repeat):
        break
    if step == TARGET_STEP:
        s = 0
        for moon in moons:
            s += moon.energy()
        print('Total energy after step ' + str(step) + ':')
        print(s)
    step += 1
    for moon in moons:
        for other_moon in moons:
            moon.velocity += np.sign(other_moon.position - moon.position)
    for moon in moons:
        moon.position += moon.velocity
print(np.lcm.reduce(repeat))
