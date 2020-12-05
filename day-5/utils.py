def read_boarding_passes():
    with open("./input.txt") as f:
        boarding_passes = f.read().splitlines()
    return boarding_passes
