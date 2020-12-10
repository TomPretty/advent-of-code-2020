from grid import Grid


def num_trees_hit(slope_x: int, slope_y: int, grid: Grid) -> int:
    x = 0
    y = 0

    num_trees = 0

    while True:
        x += slope_x
        y += slope_y

        if y >= grid.num_rows:
            break

        if grid.is_tree(x, y):
            num_trees += 1

    return num_trees
