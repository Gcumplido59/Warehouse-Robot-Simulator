class Package:
    """Represents a package to be collected in the warehouse.

    Attributes:
        row (int): The row position of the package on the grid.
        column (int): The column position of the package on the grid.
    """
    def __init__(self, row, column):
        self.row = row
        self.column = column