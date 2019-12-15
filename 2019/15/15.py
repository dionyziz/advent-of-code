from computer import Computer
from collections import deque

DIR_NORTH = 1
DIR_SOUTH = 2
DIR_WEST = 3
DIR_EAST = 4

DIRECTIONS = [-1j, 1j, -1, 1]

instruction_from_direction = {
    -1j: DIR_NORTH,
    1j: DIR_SOUTH,
    -1: DIR_WEST,
    1: DIR_EAST
}

LOC_OPEN = '.'
LOC_WALL = '#'

RESP_FAIL = 0
RESP_MOVED = 1
RESP_FOUND = 2

def shortest_path(world, src, dst):
    q = [src]
    visited = set()
    parent = {}
    while len(q):
        node = q.pop()
        visited.add(node)
        if node == dst:
            path = [node]
            while node != src:
                node = parent[node]
                path.append(node)
            path.reverse()
            return path
        for delta in DIRECTIONS:
            neighbour = node + delta
            if neighbour in world and world[neighbour] == LOC_OPEN \
            or neighbour not in world and neighbour == dst:
                if not neighbour in visited:
                    q.append(neighbour)
                    parent[neighbour] = node

def print_world(world):
    locations = list(world.keys())
    real = list(map(lambda x: int(x.real), locations))
    imag = list(map(lambda x: int(x.imag), locations))
    for y in range(min(imag), max(imag) + 1):
        row = []
        for x in range(min(real), max(real) + 1):
            node = x + y * 1j
            if node == 0:
                row.append('X')
            elif node in world:
                row.append(world[node])
            else:
                row.append('?')
        print(''.join(row))

def solve():
    def move_step(direction):
        computer.write_to(instruction_from_direction[direction])
        return computer.read_from()

    def go_to(target):
        nonlocal current_location
        nonlocal oxygen_location

        path = shortest_path(world, current_location, target)
        if path is None:
            return False, []
        path = path[1:]
        for node in path:
            delta = node - current_location
            response = move_step(delta)
            if response != RESP_FAIL:
                current_location = node
            if node == target:
                if response == RESP_FOUND:
                    solution = shortest_path(world, 0, target)[1:]
                    oxygen_location = target
                    print('Found at: ' + str(len(solution)))
                if response == RESP_FAIL:
                    world[node] = LOC_WALL
                    return False, []
                world[node] = LOC_OPEN
                ret = []
                for delta in DIRECTIONS:
                    if node + delta not in world:
                        ret.append(node + delta)
                return response == RESP_FOUND, ret
            assert(response != RESP_FAIL)

    computer = Computer()
    computer.load_file('15.txt')
    computer.execute()

    current_location = 0
    oxygen_location = None

    world = {}
    world[0] = LOC_OPEN
    unexplored = deque()
    for delta in DIRECTIONS:
        unexplored.append(current_location + delta)

    while len(unexplored):
        node = unexplored.popleft()
        found, frontier = go_to(node)
        unexplored.extend(frontier)

    diameter = 0
    for location in world.keys():
        if world[location] == LOC_OPEN:
            distance = len(shortest_path(world, oxygen_location, location)[1:])
            diameter = max(diameter, distance)
    print('Diameter: ' + str(diameter))

solve()
