from parse import parse_rules_dec

with open("./input.txt") as f:
    raw_input = f.read().splitlines()

rules = parse_rules_dec(raw_input)


def sum_of_contained_bags(bag):
    contained = rules[bag]

    num_bags = 0
    for quantity, container in contained:
        num_bags += quantity * (1 + sum_of_contained_bags(container))
    return num_bags


print(f"total contained bags: {sum_of_contained_bags('shiny gold')}")
