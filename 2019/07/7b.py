from computer import Computer, System, Pipe
from itertools import permutations

with open("7.txt") as f:
    code = f.read()

code = list(map(int, code.split(',')))

def solve():
    NUM_AMPS = 5
    bestsignal = 0
    for permutation in permutations(range(NUM_AMPS, 2 * NUM_AMPS)):
        system = System()
        for i, phase in enumerate(permutation):
            computer = Computer()
            computer.load(code)
            system.add(computer)
            if i == 0:
                first_computer = computer
            else:
                pipe = system.connect(prev_computer, computer)
                pipe.write_silent(phase)
            prev_computer = computer
        feedback_pipe = system.connect(prev_computer, first_computer)
        feedback_pipe.write_silent(permutation[0])
        feedback_pipe.write(0)

        signal = feedback_pipe.read()
        bestsignal = max(signal, bestsignal)

    return bestsignal

print(solve())
