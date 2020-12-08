from errors import InfiniteLoopError


class Processor:
    def __init__(self, instructions):
        self.instructions = instructions
        self._program_counter = 0
        self._program_counter_values = [0]
        self.acc = 0

    def execute(self):
        while self.program_counter < len(self.instructions):
            op_code, operand = self.instructions[self.program_counter]
            if op_code == "nop":
                self.execute_noop()
            elif op_code == "acc":
                self.execute_acc(operand)
            elif op_code == "jmp":
                self.execute_jmp(operand)

    def execute_noop(self):
        self.program_counter += 1

    def execute_acc(self, operand):
        self.acc += operand
        self.program_counter += 1

    def execute_jmp(self, operand):
        self.program_counter += operand

    @property
    def program_counter(self):
        return self._program_counter

    @program_counter.setter
    def program_counter(self, value):
        if value in self._program_counter_values:
            raise InfiniteLoopError()
        self._program_counter = value
        self._program_counter_values.append(value)
