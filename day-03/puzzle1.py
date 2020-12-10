from grid import Grid
from trees import num_trees_hit
from utils import get_raw_grid

raw_grid = get_raw_grid()
grid = Grid(raw_grid)

num_trees = num_trees_hit(slope_x=3, slope_y=1, grid=grid)

print(f"num_trees: {num_trees}")
