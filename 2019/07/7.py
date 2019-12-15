from computer import Computer

with open("7.txt") as f:
    code = f.read()

code = list(map(int, code.split(',')))

from itertools import permutations
from unittest.mock import Mock

def solve():
    NUM_AMPS = 5
    bestsignal = 0
    for permutation in permutations(range(NUM_AMPS)):
        signal = 0
        for phase in permutation:
            computer = Computer()
            computer.load(code)

            def in_func():
                yield phase
                yield signal

            computer.input_func = in_func
            signal = next(computer.execute())
        bestsignal = max(signal, bestsignal)
    return bestsignal

print(solve())
