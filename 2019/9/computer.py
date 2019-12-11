from inspect import signature
from collections import defaultdict, deque

OP_ADD = 1
OP_MUL = 2
OP_IN = 3
OP_OUT = 4
OP_HALT = 99
OP_JMPT = 5
OP_JMPF = 6
OP_LT = 7
OP_EQ = 8
OP_REL = 9

MEMORY_POSITION = 0
MEMORY_RELATIVE = 2
MEMORY_IMMEDIATE = 1

class IOAction(Exception):
    pass

class IOInputAction(IOAction):
    def __init__(self):
        self.value = None

class IOOutputAction(IOAction):
    def __init__(self, value):
        self.value = value

class Pipe:
    def __init__(self):
        self.data = deque()
        self.subscribers = []

    def __repr__(self):
        return self.name

    def write_silent(self, x):
        self.data.appendleft(x)

    def write(self, x):
        self.write_silent(x)
        for subscriber in self.subscribers:
            subscriber()

    def read(self):
        return self.data.pop()

    def subscribe(self, cb):
        self.subscribers.append(cb)

    def empty(self):
        return len(self.data) == 0

class System:
    def __init__(self):
        self.computers = {}
        self.pipes = {}

    def add(self, computer):
        self.computers[computer] = {
            'computer': computer,
            'state': computer.execute(),
        }

    def connect(self, source, target):
        pipe = Pipe()
        action = None
        self.pipes[source] = pipe

        def data_available():
            nonlocal action

            while self.computers[target]['state'] is not None:
                if isinstance(action, IOInputAction):
                    if pipe.empty():
                        return
                    action.value = pipe.read()
                try:
                    action = next(self.computers[target]['state'])
                except StopIteration:
                    self.computers[target]['state'] = None
                    break
                if isinstance(action, IOOutputAction):
                    self.pipes[target].write(action.value)
                elif isinstance(action, IOInputAction):
                    pending_action = action
                    if pipe.empty():
                        break

        pipe.subscribe(data_available)
        return pipe

class Computer:
    _handlers = {}
    _num_params = {}

    class ExecutionCompleted(Exception):
        pass

    def __repr__(self):
        return self.name

    def __init__(self):
        self._init_handlers()
        self.program = []
        self._current_opcode = None
        self._program = None
        self._base = 0

    def __repr__(self):
        return self.name

    def _handle(self, operation):
        def decorate(func):
            self._handlers[operation] = func
            sig = signature(func)
            self._num_params[operation] = len(sig.parameters.items()) - 1
            return func
        return decorate

    def _jump(self, ip):
        self._ip = ip
        self._ip_manual = True

    def _dispatch(self, operation, handler, opcode):
        args = []
        for i in range(1, self._num_params[operation] + 1):
            args.append(self._read(i, opcode))
        ret = handler(self, *args)
        if ret is not None:
            yield from ret
        if self._ip_manual:
            self._ip_manual = False
        else:
            self._ip += self._num_params[operation] + 1

    def _init_handlers(self):
        @self._handle(OP_ADD)
        def _add(self, x, y, _):
            self._write(3, x + y)

        @self._handle(OP_MUL)
        def _mul(self, x, y, _):
            self._write(3, x * y)

        @self._handle(OP_IN)
        def _in(self, _):
            action = IOInputAction()
            yield action
            if action.value is None:
                raise ValueError('No input provided')
            self._write(1, action.value)

        @self._handle(OP_OUT)
        def _out(self, x):
            yield IOOutputAction(x)

        @self._handle(OP_LT)
        def _lt(self, x, y, _):
            self._write(3, x < y)

        @self._handle(OP_EQ)
        def _eq(self, x, y, _):
            self._write(3, x == y)

        @self._handle(OP_HALT)
        def _halt(self):
            raise self.ExecutionCompleted

        @self._handle(OP_JMPT)
        def _jmpt(self, cond, target):
            if cond:
                self._jump(target)

        @self._handle(OP_JMPF)
        def _jmpf(self, cond, target):
            if not cond:
                self._jump(target)

        @self._handle(OP_REL)
        def _rel(self, base):
            self._base += base

    def _getmode(self, i, opcode):
        return (opcode // 10**(i + 1)) % 10

    def _read(self, i, opcode):
        loc = self.memory[self._ip + i]
        mode = self._getmode(i, opcode)
        return {
            MEMORY_POSITION: self.memory[loc],
            MEMORY_RELATIVE: self.memory[self._base + loc],
            MEMORY_IMMEDIATE: loc
        }[mode]

    def _write(self, i, val, opcode=None):
        if opcode is None:
            opcode = self._current_opcode
        op_loc = self.memory[self._ip + i]
        mode = self._getmode(i, opcode)
        if mode == MEMORY_POSITION:
            self.memory[op_loc] = int(val)
        elif mode == MEMORY_RELATIVE:
            self.memory[self._base + op_loc] = int(val)
        else:
            raise 'Invalid memory mode for writing ' + str(mode)

    def _init_memory(self):
        self.memory = defaultdict(lambda: 0)
        for i, instruction in enumerate(self._program):
            self.memory[i] = instruction

    def load(self, program):
        self._program = program

    def load_file(self, filename):
        with open(filename) as f:
            code = f.read()

        code = list(map(int, code.split(',')))
        self.load(code)

    def read_from(self, iter):
        action = next(iter)
        assert(isinstance(action, IOOutputAction))
        return action.value

    def write_to(self, iter, value):
        action = next(iter)
        assert(isinstance(action, IOInputAction))
        action.value = value

    def execute(self):
        self._ip = 0
        self._ip_manual = False
        self._init_memory()
        while self._ip < len(self.memory):
            opcode = self.memory[self._ip]
            self._current_opcode = opcode
            operation = opcode % 100
            if operation not in self._handlers:
                raise ValueError('Invalid opcode ' + str(opcode))
            try:
                handler = self._handlers[operation]
                action = self._dispatch(operation, handler, opcode)
                if action is not None:
                    yield from action
            except self.ExecutionCompleted:
                break
        else:
            raise EOFError('Reached program end without halting')

    def run(self):
        for action in self.execute():
            if isinstance(action, IOInputAction):
                action.value = input('Input: ')
            elif isinstance(action, IOOutputAction):
                print(action.value)
