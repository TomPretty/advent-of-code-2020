with open("./input.txt") as f:
    tokens = f.read().splitlines()


def parse_group(tokens):
    group = []
    while True:
        group.append(list(tokens.pop(0)))

        if not tokens or not tokens[0]:
            break
    return group


def parse_groups(tokens):
    groups = []
    while True:
        groups.append(parse_group(tokens))

        if tokens:
            tokens.pop(0)
        else:
            break
    return groups


groups = parse_groups(tokens)


def union_of_answered_questions(group):
    union = set(group[0])
    for answers in group[1:]:
        union = union.union(answers)
    return union


unions = [union_of_answered_questions(group) for group in groups]

print(f"sum of length of unions: {sum(len(u) for u in unions)}")


def intersection_of_answered_questions(group):
    intersection = set(group[0])
    for answers in group[1:]:
        intersection = intersection.intersection(answers)
    return intersection


intersections = [intersection_of_answered_questions(group) for group in groups]

print(f"sum of length of intersections: {sum(len(i) for i in intersections)}")
