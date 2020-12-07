from parse import parse_rules

with open("./input.txt") as f:
    raw_input = f.read().splitlines()

rules = parse_rules(raw_input)

containers = set()
frontier = rules["shiny gold"]

while frontier:
    _, container = frontier.pop(0)

    containers.add(container)

    frontier += rules[container]

print(f"number of containers: {len(containers)}")
