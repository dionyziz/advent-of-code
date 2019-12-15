OP_ADD = 1
OP_MUL = 2
OP_IN = 3
OP_OUT = 4
OP_HALT = 99
OP_JMPT = 5
OP_JMPF = 6
OP_LT = 7
OP_EQ = 8

num_params = {
    OP_ADD: 3,
    OP_MUL: 3,
    OP_IN: 1,
    OP_OUT: 1,
    OP_HALT: 0,
    OP_JMPT: 2,
    OP_JMPF: 2,
    OP_LT: 3,
    OP_EQ: 3
}

with open("5.txt") as f:
    program = f.read()
# program = "3,0,4,0,99"
# program = "3,9,8,9,10,9,4,9,99,-1,8"
# program = "3,9,7,9,10,9,4,9,99,-1,8"
# program = "3,3,1108,-1,8,3,4,3,99"
# program = "3,3,1107,-1,8,3,4,3,99"
# program = "3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9"
# program = "3,3,1105,-1,9,1101,0,0,12,4,12,99,1"
# program = "3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,"\
# "1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,"\
# "999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99"
program = list(map(int, program.split(',')))

def read(memory, ip, i, opcode):
    loc = memory[ip + i]
    if (opcode // 10**(i + 1)) % 10 == 0:
        return memory[loc]
    return loc

def write(memory, ip, i, val):
    op_loc = memory[ip + i]
    memory[op_loc] = val

def run(program):
    memory = {}
    for i, instruction in enumerate(program):
        memory[i] = instruction

    ip = 0
    while ip < len(program):
        opcode = memory[ip]
        operation = opcode % 100
        # print("Operation: " + str(operation))
        if operation == OP_HALT:
            break
        elif operation == OP_MUL or operation == OP_ADD:
            lval = read(memory, ip, 1, opcode)
            rval = read(memory, ip, 2, opcode)
            if operation == OP_ADD:
                res = lval + rval
            elif operation == OP_MUL:
                res = lval * rval
            write(memory, ip, 3, res)
        elif operation == OP_IN:
            s = int(input('Input: '))
            write(memory, ip, 1, int(s))
        elif operation == OP_OUT:
            s = read(memory, ip, 1, opcode)
            print('Output: ' + str(s))
        elif operation == OP_JMPT:
            val = read(memory, ip, 1, opcode)
            if val != 0:
                ip = read(memory, ip, 2, opcode)
                continue
        elif operation == OP_JMPF:
            val = read(memory, ip, 1, opcode)
            if val == 0:
                ip = read(memory, ip, 2, opcode)
                continue
        elif operation == OP_LT:
            lval = read(memory, ip, 1, opcode)
            rval = read(memory, ip, 2, opcode)
            if lval < rval:
                out = 1
            else:
                out = 0
            write(memory, ip, 3, out)
        elif operation == OP_EQ:
            lval = read(memory, ip, 1, opcode)
            rval = read(memory, ip, 2, opcode)
            if lval == rval:
                out = 1
            else:
                out = 0
            write(memory, ip, 3, out)
        else:
            print('Invalid opcode ' + str(opcode))
        ip += num_params[operation] + 1
    else:
        print('Reached program end without halting')

    return memory[0]

run(program)
