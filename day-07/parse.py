from collections import defaultdict


def parse_rules(rules):
    parsed = defaultdict(list)
    for rule in rules:
        parsed_rule = parse_rule(rule)
        if parsed_rule:
            for contained, quantity, container in parsed_rule:
                parsed[contained].append((quantity, container))
    return parsed


def parse_rules_dec(rules):
    parsed = defaultdict(list)
    for rule in rules:
        parsed_rule = parse_rule(rule)
        if parsed_rule:
            for contained, quantity, container in parsed_rule:
                parsed[container].append((quantity, contained))
    return parsed


def parse_rule(rule):
    if "no other bags" in rule:
        return None

    tokens = rule.split(" ")

    container = parse_bag(tokens)
    tokens.pop(0)  # contain

    quantities = []
    bags = []

    while tokens:
        quantities.append(parse_quantity(tokens))
        bags.append(parse_bag(tokens))

    return ((bag, quantity, container) for bag, quantity in zip(bags, quantities))


def parse_quantity(tokens):
    return int(tokens.pop(0))


def parse_bag(tokens):
    adjective = tokens.pop(0)
    colour = tokens.pop(0)
    tokens.pop(0)  # bags

    return f"{adjective} {colour}"
