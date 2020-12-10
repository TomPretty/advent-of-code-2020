def read_instructions():
    with open("./input.txt") as f:
        lines = f.read().splitlines()

    def parse_instruction(line):
        op_code, operand = line.split(" ")
        return (op_code, int(operand))

    return [parse_instruction(line) for line in lines]
