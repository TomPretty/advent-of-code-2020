import operator
from functools import reduce

from grid import Grid
from trees import num_trees_hit
from utils import get_raw_grid

raw_grid = get_raw_grid()
grid = Grid(raw_grid)

slopes = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
]

num_trees = [num_trees_hit(slope_x, slope_y, grid) for slope_x, slope_y in slopes]

ans = reduce(operator.mul, num_trees, 1)

print(f"ans: {ans}")
