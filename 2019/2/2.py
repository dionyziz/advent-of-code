OP_ADD = 1
OP_MUL = 2
OP_HALT = 99

with open("2.txt") as f:
    program = f.read()
program = list(map(int, program.split(',')))

def run(program, input):
    memory = {}
    for i, instruction in enumerate(program):
        memory[i] = instruction

    memory[1] = input[0]
    memory[2] = input[1]

    pc = 0
    while pc < len(program):
        opcode = memory[pc]
        if opcode == OP_HALT:
            break
        lop = memory[pc + 1]
        rop = memory[pc + 2]
        target = memory[pc + 3]
        lval = memory[lop]
        rval = memory[rop]
        if opcode == OP_ADD:
            res = lval + rval
        elif opcode == OP_MUL:
            res = lval * rval
        memory[target] = res
        pc += 4

    return memory[0]

print(run(program, [12, 2]))

for noun in range(100):
    for verb in range(100):
        if run(program, [noun, verb]) == 19690720:
            print(100 * noun + verb)
