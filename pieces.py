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
        print("Pawn moves forward 1 position")

class Rook(BaseChessPiece):
    def __init__(self, color, identifier):
        super().__init__(color, identifier, "Rook", 'R')

    def move(self):
        print("Rook moves in a straight line")

class Bishop(BaseChessPiece):
    def __init__(self, color, identifier):
        super().__init__(color, identifier, "Bishop", 'B')

    def move(self):
        print("Bishop moves diagonally")

class Queen(BaseChessPiece):
    def __init__(self, color, identifier):
        super().__init__(color, identifier, "Queen", 'Q')

    def move(self):
        print("Queen moves in a straight line and diagonally")

class King(BaseChessPiece):
    def __init__(self, color, identifier):
        super().__init__(color, identifier, "King", 'K')

    def move(self):
        print("King moves one position in any direction")

class Knight(BaseChessPiece):
    def __init__(self, color, identifier):
        super().__init__(color, identifier, "Knight", 'N')

    def move(self):
        print("Knight moves in an L shape")