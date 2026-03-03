from abc import ABC, abstractmethod

class BaseChessPiece(ABC):
    def __init__(self, color, identifier, name, symbol):
        self.color = color
        self.identifier = identifier
        self.name = name
        self.symbol = symbol
        self.position = None
        self.is_alive = True

    @abstractmethod
    def move(self):
        pass

    def move_piece(self, movement):
        print(movement)

    def die(self):
        self.is_alive = False

    def __str__(self):
        return f"{self.color} {self.name} {self.identifier}"

    def __repr__(self):
        return self.__str__()

class Pawn(BaseChessPiece):
    def __init__(self, color, identifier):
        super().__init__(color, identifier, "Pawn", '-')

    def move(self):
        movement = "Pawn moves forward 1 position"
        super().move_piece(movement)

class Rook(BaseChessPiece):
    def __init__(self, color, identifier):
        super().__init__(color, identifier, "Rook", 'R')

    def move(self):
        movement = "Rook moves in a straight line"
        super().move_piece(movement)

class Bishop(BaseChessPiece):
    def __init__(self, color, identifier):
        super().__init__(color, identifier, "Bishop", 'B')

    def move(self):
        movement = "Bishop moves diagonally"
        super().move_piece(movement)

class Queen(BaseChessPiece):
    def __init__(self, color, identifier):
        super().__init__(color, identifier, "Queen", 'Q')

    def move(self):
        movement = "Queen moves in a straight line and diagonally"
        super().move_piece(movement)

class King(BaseChessPiece):
    def __init__(self, color, identifier):
        super().__init__(color, identifier, "King", 'K')

    def move(self):
        movement = "King moves one position in any direction"
        super().move_piece(movement)

class Knight(BaseChessPiece):
    def __init__(self, color, identifier):
        super().__init__(color, identifier, "Knight", 'N')

    def move(self):
        movement = "Knight moves in an L shape"
        super().move_piece(movement)
