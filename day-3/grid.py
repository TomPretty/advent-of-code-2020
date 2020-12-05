class Grid:
    def __init__(self, grid: str) -> None:
        self.rows = [row for row in grid.split("\n") if row]

    @property
    def num_rows(self) -> int:
        return len(self.rows)

    @property
    def num_cols(self) -> int:
        return len(self.rows[0])

    def is_tree(self, x: int, y: int) -> bool:
        x = x % self.num_cols

        return self.rows[y][x] == "#"
