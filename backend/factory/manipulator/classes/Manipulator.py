from .Grid import factory_grid
import sys


class Manipulator:
    grid = []
    x = 0
    y = 0
    is_grabbed = False

    def __init__(self, grid):
        self.grid = grid.get_grid()
        self.grid[0][0] = 'm'

    def __in_borders(self, x, y) -> bool:
        if 0 <= y < len(self.grid) and 0 <= x < len(self.grid[0]):
            return True

    def move(self, command):
        x, y = self.x, self.y
        if command == "up":
            if self.__in_borders(x, y - 1):
                if self.grid[y - 1][x] != 1:
                    y -= 1
        elif command == 'down':
            if self.__in_borders(x, y + 1):
                if self.grid[y + 1][x] != 1:
                    y += 1
        elif command == 'left':
            if self.__in_borders(x - 1, self.y):
                if self.grid[y][x - 1] != 1:
                    x -= 1
        elif command == 'right':
            if self.__in_borders(x + 1, y):
                if self.grid[y][x + 1] != 1:
                    x += 1
        elif command == 'grab':
            self.grab()
        if self.x != x or self.y != y:
            self.grid[y][x] = 'm'
            self.grid[self.y][self.x] = 0
            self.x, self.y = x, y
        print(self.grid, file=sys.stderr)

    def grab(self):
        if not self.is_grabbed:
            if self.grid[self.y + 1][self.x] == 1:
                self.is_grabbed = True
                self.grid[self.y + 1][self.x] = 0
        else:
            if self.grid[self.y + 1][self.x] == 0:
                self.is_grabbed = False
                self.grid[self.y + 1][self.x] = 1

    def load_grid(self, grid):
        for i in range(len(grid)):
            if grid[i] == 'm':
                self.x = i % 16
                self.y = i // 16
                factory_grid.grid[i // 16][i % 16] = grid[i]
            else:
                factory_grid.grid[i // 16][i % 16] = int(grid[i])

        self.grid = factory_grid.get_grid()


manipulator = Manipulator(factory_grid)
