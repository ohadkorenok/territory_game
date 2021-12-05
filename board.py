from random import randint
from cell import Cell
from territory import Territory


class Board:
    """
    This class represents a board.
    Every board has cells array and territory.
    At initialization we create a board, and init the territory of a the board to be the upper left cell.
    """
    colors = ['g', 'b', 'y', 'r']

    def __init__(self, dimensions=18):
        self.cells = []
        for row in range(0, dimensions):
            row_arr = []
            for col in range(0, dimensions):
                color_index = randint(0, len(self.colors) - 1)
                color = self.colors[color_index]
                cell = Cell(color=color, row=row, column=col)
                row_arr.append(cell)
            self.cells.append(row_arr)
        self.territory = Territory(self.cells[0][0])
        print("INIT STARTED\n################")
        self.print_board()
        self.expand_territory()
        print("AFTER EXPANSION\n################")

        self.print_board()

    def get_neighbors(self, cell: Cell) -> list:
        neighbors = []
        if cell.row > 0:  # For left
            neighbors.append(self.cells[cell.row - 1][cell.column])
        if cell.column > 0:
            neighbors.append(self.cells[cell.row][cell.column - 1])  # Upper neighbor
        if cell.row < len(self.cells) - 1:
            neighbors.append(self.cells[cell.row + 1][cell.column])
        if cell.column < len(self.cells[0]) - 1:
            neighbors.append(self.cells[cell.row][cell.column + 1])
        return neighbors

    def expand_territory(self):
        """
        This method expands the territory. It does it by scanning in a BFS manner over all of the boundary cells of the
        territory. Later on, It appends the neighbors to the cells and boundaries.
        As a result, our territory got expanded.

        INV:: Change color will be called before.
        """
        visited = set()
        queue = []
        for cell in self.territory.boundaries:
            queue.append(cell)
            visited.add(cell)
        while queue:
            cell = queue.pop(0)
            for neighbor in self.get_neighbors(cell):
                if neighbor not in self.territory.cells and neighbor.color == self.territory.color \
                        and neighbor not in visited:
                    self.territory.cells.add(neighbor)
                    self.territory.counter += 1
                    self.territory.boundaries.append(neighbor)
                    queue.append(neighbor)
                    # We work abroad here

    def remove_boundaries(self):
        """This method scans the territory boundaries to check whether some cells got absorbed the territory."""
        for cell in self.territory.boundaries:
            if all([i.color == cell.color for i in self.get_neighbors(cell)]):
                self.territory.boundaries.remove(cell)
                print(f"cell {cell} has been removed from boundaries")

    def validate_color(self, color):
        if color not in self.colors:
            raise ValueError(
                f"Color {color} is not a valid color! please enter valid color from the list : {self.colors}")

    def check_end_game(self):
        return self.territory.counter == len(self.cells) ** 2

    def move(self, color):
        print(f"Move got color {color}")
        self.change_territory_color(color)
        self.expand_territory()
        self.remove_boundaries()
        self.print_board()
        return self.check_end_game()

    def print_board(self):
        for row in self.cells:
            print([cell.color for cell in row])
        print("###############")
        print(self.territory)
        print("##############################")

    def change_territory_color(self, color):
        """Change territory color"""
        self.validate_color(color)
        self.territory.change_color(color)
