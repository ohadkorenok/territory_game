class Cell:
    """
    This class represents a cell.
    Every cell has color.
    For easier track, we also save the row and column indexes of the cell.
    """
    def __init__(self, color, row, column):
        self.color = color
        self.row = row
        self.column = column

    def __str__(self):
        return f"Cell[{self.row}][{self.column}]. color: {self.color}"

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash((self.row, self.column))
