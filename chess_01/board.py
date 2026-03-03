class Board:
    def __init__(self):
        # Create a dictionary to represent the chess board
        self.squares = {}

        # Populate the dictionary with keys for each square on the board
        for col in range(ord('a'), ord('i')):  # Columns a-h
            for row in range(1, 9):            # Rows 1-8
                square_name = f"{chr(col)}{row}"
                self.squares[square_name] = None
