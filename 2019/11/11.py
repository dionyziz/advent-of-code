from computer import Computer
from collections import defaultdict

computer = Computer()
computer.load_file("11.txt")
color_at = defaultdict(lambda: 0)

def paint(computer, color_at):
    modified = set()
    direction = 1j
    location = 0
    execution = computer.execute()

    while True:
        try:
            computer.write_to(color_at[location])
            color_at[location] = computer.read_from()
            modified.add((int(location.real), int(location.imag)))
            turn = computer.read_from()
            direction *= 1j
            direction *= turn * 2 - 1
            location += direction
        except StopIteration:
            return modified

print(len(paint(computer, color_at)))
color_at = defaultdict(lambda: 0)
color_at[0] = 1
modified = paint(computer, color_at)
xs, ys = zip(*list(modified))
for y in reversed(range(min(ys), max(ys) + 1)):
    row = []
    for x in reversed(range(min(xs), max(xs) + 1)):
        if color_at[x + y * 1j] == 0:
            row.append('.')
        else:
            row.append('#')
    print(''.join(row))
