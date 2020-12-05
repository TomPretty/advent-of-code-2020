import math


def parse_bsp_location(bsp, left_char, right_char, lower, upper):
    for c in bsp:
        if c == left_char:
            upper = math.floor(upper - (upper - lower) / 2)
        elif c == right_char:
            lower = math.ceil(lower + (upper - lower) / 2)
    assert lower == upper

    return lower


def parse_boarding_pass(boarding_pass):
    row = parse_bsp_location(
        boarding_pass[:7], left_char="F", right_char="B", lower=0, upper=127
    )
    col = parse_bsp_location(
        boarding_pass[7:], left_char="L", right_char="R", lower=0, upper=7
    )

    return row * 8 + col
