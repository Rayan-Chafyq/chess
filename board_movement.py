class BoardMovement:
    @staticmethod
    def forward(position: str, color: str, squares: int = 1):
        """Move the piece forward on the board."""
        column = position[0]
        row = int(position[1])
        new_row = row + (1 * (-1 if color == 'WHITE' else 1) * squares)
        if new_row < 1 or new_row > 8:
            return None
        return f"{column}{new_row}"

    @staticmethod
    def backward(position: str, color: str, squares: int = 1):
        """Move the piece backward on the board."""
        column = position[0]
        row = int(position[1])
        new_row = row + (-1 * (-1 if color == 'WHITE' else 1) * squares)
        if new_row < 1 or new_row > 8:
            return None
        return f"{column}{new_row}"

    @staticmethod
    def left(position: str, squares: int = 1):
        """Move the piece left on the board."""
        column = position[0]
        row = int(position[1])
        new_column = chr(ord(column) - squares)
        if new_column < 'a' or new_column > 'h':
            return None
        return f"{new_column}{row}"

    @staticmethod
    def right(position: str, squares: int = 1):
        """Move the piece right on the board."""
        column = position[0]
        row = int(position[1])
        new_column = chr(ord(column) + squares)
        if new_column < 'a' or new_column > 'h':
            return None
        return f"{new_column}{row}"

    @staticmethod
    def diagonal_forward_left(position: str, color: str, squares: int = 1):
        """Move the piece diagonally forward and left on the board."""
        column = position[0]
        row = int(position[1])
        new_column = chr(ord(column) - squares)
        new_row = row + (1 * (-1 if color == 'WHITE' else 1) * squares)
        if new_column < 'a' or new_column > 'h' or new_row < 1 or new_row > 8:
            return None
        return f"{new_column}{new_row}"

    @staticmethod
    def diagonal_forward_right(position: str, color: str, squares: int = 1):
        """Move the piece diagonally forward and right on the board."""
        column = position[0]
        row = int(position[1])
        new_column = chr(ord(column) + squares)
        new_row = row + (1 * (-1 if color == 'WHITE' else 1) * squares)
        if new_column < 'a' or new_column > 'h' or new_row < 1 or new_row > 8:
            return None
        return f"{new_column}{new_row}"

    @staticmethod
    def diagonal_backward_left(position: str, color: str, squares: int = 1):
        """Move the piece diagonally backward and left on the board."""
        column = position[0]
        row = int(position[1])
        new_column = chr(ord(column) - squares)
        new_row = row + (-1 * (-1 if color == 'WHITE' else 1) * squares)
        if new_column < 'a' or new_column > 'h' or new_row < 1 or new_row > 8:
            return None
        return f"{new_column}{new_row}"

    @staticmethod
    def diagonal_backward_right(position: str, color: str, squares: int = 1):
        """Move the piece diagonally backward and right on the board."""
        column = position[0]
        row = int(position[1])
        new_column = chr(ord(column) + squares)
        new_row = row + (-1 * (-1 if color == 'WHITE' else 1) * squares)
        if new_column < 'a' or new_column > 'h' or new_row < 1 or new_row > 8:
            return None
        return f"{new_column}{new_row}"

    @staticmethod
    def knight_move(position: str, direction: str):
        """Move the piece in an L-shape, specific for knights."""
        column = position[0]
        row = int(position[1])

        if direction == 'forward-left':
            new_column = chr(ord(column) - 1)
            new_row = row + 2
        elif direction == 'forward-right':
            new_column = chr(ord(column) + 1)
            new_row = row + 2
        elif direction == 'backward-left':
            new_column = chr(ord(column) - 1)
            new_row = row - 2
        elif direction == 'backward-right':
            new_column = chr(ord(column) + 1)
            new_row = row - 2
        elif direction == 'left-forward':
            new_column = chr(ord(column) - 2)
            new_row = row + 1
        elif direction == 'left-backward':
            new_column = chr(ord(column) - 2)
            new_row = row - 1
        elif direction == 'right-forward':
            new_column = chr(ord(column) + 2)
            new_row = row + 1
        elif direction == 'right-backward':
            new_column = chr(ord(column) + 2)
            new_row = row - 1
        else:
            return None

        if new_column < 'a' or new_column > 'h' or new_row < 1 or new_row > 8:
            return None
        return f"{new_column}{new_row}"
