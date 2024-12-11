import sys


class Grid:
    grid = []

    def __init__(self):
        self.reset()

    def __getitem__(self, k):
        return self.grid[k]

    def reset(self):
        self.grid = [[0] * 16 for x in range(12)]
        [self.grid.append([1] * 16) for x in range(4)]

    def get_grid(self):
        return self.grid


factory_grid = Grid()
