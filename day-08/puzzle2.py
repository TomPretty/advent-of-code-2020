from errors import InfiniteLoopError
from processor import Processor
from utils import read_instructions

instructions = read_instructions()

possible_instructions = []
for i in range(len(instructions)):
    op_code, operand = instructions[i]
    if op_code == "jmp":
        new_instructions = instructions.copy()
        new_instructions[i] = ("nop", operand)
        possible_instructions.append(new_instructions)
    if op_code == "nop":
        new_instructions = instructions.copy()
        new_instructions[i] = ("jmp", operand)
        possible_instructions.append(new_instructions)


for instructions in possible_instructions:
    processor = Processor(instructions)

    try:
        processor.execute()
        print(f"acc: {processor.acc}")
        break
    except InfiniteLoopError as _:
        continue
