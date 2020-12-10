from errors import InfiniteLoopError
from processor import Processor
from utils import read_instructions

instructions = read_instructions()
processor = Processor(instructions)

try:
    processor.execute()
except InfiniteLoopError as _:
    print(f"acc: {processor.acc}")
