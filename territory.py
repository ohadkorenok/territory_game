class Territory:
    """
    This class is used to manage and track the one-color sequence. We call it territory.
    Boundaries array represents the boundaries of the sequence. Why? because our territory will expand by our boundaries
    Color - the current color of the territory
    Counter for calculating the number of cells in the territory.
    Cells - Set representing all of the cells in the territory
    """
    def __init__(self, starting_cell):
        self.cells = {starting_cell}  # Set keys in the format of row_col
        self.boundaries = [starting_cell]  # Array of boundary cells need to check
        self.color = starting_cell.color
        self.counter = 1

    def __repr__(self):
        return f"Territory:\ncolor: {self.color}\ncount: {self.counter}\nboundaries: {self.boundaries}\n"

    def change_color(self, color):
        """This method changes color to the territory and its cells."""
        self.color = color
        for cell in self.cells:
            cell.color = color
