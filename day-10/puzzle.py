with open("./input.txt") as f:
    raw_input = [int(l) for l in f.read().splitlines()]

voltages = [0] + sorted(raw_input) + [max(raw_input) + 3]

diffs_dist = {1: 0, 2: 0, 3: 0}

for v1, v2 in zip(voltages, voltages[1:]):
    diff = v2 - v1
    diffs_dist[diff] += 1

print(f"p1 ans: {diffs_dist[1] * diffs_dist[3]}")


def memoized(func):
    cache = {}

    def wrapped(*args):
        if args in cache:
            return cache[args]

        ans = func(*args)
        cache[args] = ans
        return ans

    return wrapped


@memoized
def num_connections(voltage):
    if voltage == 0:
        return 1

    connections = [v for v in voltages if voltage - v in [1, 2, 3]]

    return sum(num_connections(c) for c in connections)


print(f"p2 ans: {num_connections(voltages[-1])}")
