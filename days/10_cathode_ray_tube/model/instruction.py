from .register import Register


class Instruction:
    ticks_until_execution: int = 0
    register: Register = None
    executed: bool = False

    def __init__(self, ticks_until_execution: int, register: Register):
        self.ticks_until_execution = ticks_until_execution
        self.register = register
        self.executed = False

    def action(self):
        pass

    def tick(self):
        if self.ticks_until_execution >= 1:
            self.ticks_until_execution -= 1
        if self.executed == False and self.ticks_until_execution == 0:
            self.action()
            self.executed = True



class NoopInstruction(Instruction):
    NOOP_TICKS = 1
    NOOP_INSTRUCTION_NAME = "noop"

    def __init__(self, register: Register):
        super().__init__(self.NOOP_TICKS, register)

    def action(self):
        pass


class AddxInstruction(Instruction):
    ADDX_TICKS = 2
    value_to_add: int = 0
    ADDX_INSTRUCTION_NAME = "addx"


    def __init__(self, register: Register, value: int):
        self.value_to_add = value
        super().__init__(self.ADDX_TICKS, register)

    def action(self):
        self.register.perform_add(self.value_to_add)
