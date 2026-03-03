from abc import ABC, abstractmethod
import functools
import json

class BaseChessPiece(ABC):
    def __init__(self, color, identifier, name, symbol):
        self.color = color
        self.identifier = identifier
        self.name = name
        self.symbol = symbol
        self.position = None
        self.is_alive = True
        self.board = None

    @abstractmethod
    def move(self, *args, **kwargs):
        pass

    def die(self):
        self.is_alive = False

    def set_initial_position(self, position):
        self.position = position

    def define_board(self, board):
        self.board = board

    def __str__(self):
        return f"{self.color} {self.name} {self.identifier}"

    def __repr__(self):
        return self.__str__

def print_board(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        result = func(self, *args, **kwargs)
        if self.board:
            self.board.print_board()
        return result
    return wrapper

def save_board(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        result = func(self, *args, **kwargs)
        if self.board:
            self.board.save_board()
        return result
    return wrapper

class Pawn(BaseChessPiece):
    def __init__(self, color, identifier):
        super().__init__(color, identifier, "Pawn", '-')

    @print_board
    @save_board
    def move(self, squares=1):
        from board_movement import BoardMovement
        movement = BoardMovement.forward(self.position, self.color, squares)
        if movement:
            new_location = self.board.get_piece(movement)
            if new_location is None:
                self.board.squares[self.position] = None
                self.position = movement
                self.board.squares[self.position] = self

class Rook(BaseChessPiece):
    def __init__(self, color, identifier):
        super().__init__(color, identifier, "Rook", 'R')

    @print_board
    @save_board
    def move(self, direction, squares=1):
        from board_movement import BoardMovement
        if direction == 'forward':
            movement = BoardMovement.forward(self.position, self.color, squares)
        elif direction == 'backward':
            movement = BoardMovement.backward(self.position, self.color, squares)
        elif direction == 'left':
            movement = BoardMovement.left(self.position, squares)
        elif direction == 'right':
            movement = BoardMovement.right(self.position, squares)
        else:
            return

        if movement:
            new_location = self.board.get_piece(movement)
            if new_location is None:
                self.board.squares[self.position] = None
                self.position = movement
                self.board.squares[self.position] = self

class Knight(BaseChessPiece):
    def __init__(self, color, identifier):
        super().__init__(color, identifier, "Knight", 'N')

    @print_board
    @save_board
    def move(self, direction):
        from board_movement import BoardMovement
        movement = BoardMovement.knight_move(self.position, direction)
        if movement:
            new_location = self.board.get_piece(movement)
            if new_location is None:
                self.board.squares[self.position] = None
                self.position = movement
                self.board.squares[self.position] = self

class Bishop(BaseChessPiece):
    def __init__(self, color, identifier):
        super().__init__(color, identifier, "Bishop", 'B')

    @print_board
    @save_board
    def move(self, direction, squares=1):
        from board_movement import BoardMovement
        if direction == 'forward-left':
            movement = BoardMovement.diagonal_forward_left(self.position, self.color, squares)
        elif direction == 'forward-right':
            movement = BoardMovement.diagonal_forward_right(self.position, self.color, squares)
        elif direction == 'backward-left':
            movement = BoardMovement.diagonal_backward_left(self.position, self.color, squares)
        elif direction == 'backward-right':
            movement = BoardMovement.diagonal_backward_right(self.position, self.color, squares)
        else:
            return

        if movement:
            new_location = self.board.get_piece(movement)
            if new_location is None:
                self.board.squares[self.position] = None
                self.position = movement
                self.board.squares[self.position] = self

class Queen(BaseChessPiece):
    def __init__(self, color, identifier):
        super().__init__(color, identifier, "Queen", 'Q')

    @print_board
    @save_board
    def move(self, direction, squares=1):
        from board_movement import BoardMovement
        if direction in ['forward-left', 'forward-right', 'backward-left', 'backward-right']:
            if direction == 'forward-left':
                movement = BoardMovement.diagonal_forward_left(self.position, self.color, squares)
            elif direction == 'forward-right':
                movement = BoardMovement.diagonal_forward_right(self.position, self.color, squares)
            elif direction == 'backward-left':
                movement = BoardMovement.diagonal_backward_left(self.position, self.color, squares)
            elif direction == 'backward-right':
                movement = BoardMovement.diagonal_backward_right(self.position, self.color, squares)
        elif direction in ['forward', 'backward', 'left', 'right']:
            if direction == 'forward':
                movement = BoardMovement.forward(self.position, self.color, squares)
            elif direction == 'backward':
                movement = BoardMovement.backward(self.position, self.color, squares)
            elif direction == 'left':
                movement = BoardMovement.left(self.position, squares)
            elif direction == 'right':
                movement = BoardMovement.right(self.position, squares)
        else:
            return

        if movement:
            new_location = self.board.get_piece(movement)
            if new_location is None:
                self.board.squares[self.position] = None
                self.position = movement
                self.board.squares[self.position] = self

class King(BaseChessPiece):
    def __init__(self, color, identifier):
        super().__init__(color, identifier, "King", 'K')

    @print_board
    @save_board
    def move(self, direction, squares=1):
        from board_movement import BoardMovement
        if direction in ['forward-left', 'forward-right', 'backward-left', 'backward-right']:
            if direction == 'forward-left':
                movement = BoardMovement.diagonal_forward_left(self.position, self.color, 1)
            elif direction == 'forward-right':
                movement = BoardMovement.diagonal_forward_right(self.position, self.color, 1)
            elif direction == 'backward-left':
                movement = BoardMovement.diagonal_backward_left(self.position, self.color, 1)
            elif direction == 'backward-right':
                movement = BoardMovement.diagonal_backward_right(self.position, self.color, 1)
        elif direction in ['forward', 'backward', 'left', 'right']:
            if direction == 'forward':
                movement = BoardMovement.forward(self.position, self.color, 1)
            elif direction == 'backward':
                movement = BoardMovement.backward(self.position, self.color, 1)
            elif direction == 'left':
                movement = BoardMovement.left(self.position, 1)
            elif direction == 'right':
                movement = BoardMovement.right(self.position, 1)
        else:
            return

        if movement:
            new_location = self.board.get_piece(movement)
            if new_location is None:
                self.board.squares[self.position] = None
                self.position = movement
                self.board.squares[self.position] = self
