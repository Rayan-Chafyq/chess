from pieces import Pawn, Rook, Knight, Bishop, Queen, King
import json

class Board:
    def __init__(self):
        # Create a dictionary to represent the chess board
        self.squares = {}

        # Populate the dictionary with keys for each square on the board
        for col in range(ord('a'), ord('i')):  # Columns a-h
            for row in range(1, 9):            # Rows 1-8
                square_name = f"{chr(col)}{row}"
                self.squares[square_name] = None

    def setup_board(self):
        # Add Rooks
        self.squares['a1'] = Rook('BLACK', 1)
        self.squares['h1'] = Rook('BLACK', 2)
        self.squares['a8'] = Rook('WHITE', 1)
        self.squares['h8'] = Rook('WHITE', 2)

        # Add Knights
        self.squares['b1'] = Knight('BLACK', 1)
        self.squares['g1'] = Knight('BLACK', 2)
        self.squares['b8'] = Knight('WHITE', 1)
        self.squares['g8'] = Knight('WHITE', 2)

        # Add Bishops
        self.squares['c1'] = Bishop('BLACK', 1)
        self.squares['f1'] = Bishop('BLACK', 2)
        self.squares['c8'] = Bishop('WHITE', 1)
        self.squares['f8'] = Bishop('WHITE', 2)

        # Add Queens
        self.squares['d1'] = Queen('BLACK', 1)
        self.squares['d8'] = Queen('WHITE', 1)

        # Add Kings
        self.squares['e1'] = King('BLACK', 1)
        self.squares['e8'] = King('WHITE', 1)

        # Add Black Pawns on row 2
        black_pawns = {
            'a2': Pawn('BLACK', 1),
            'b2': Pawn('BLACK', 2),
            'c2': Pawn('BLACK', 3),
            'd2': Pawn('BLACK', 4),
            'e2': Pawn('BLACK', 5),
            'f2': Pawn('BLACK', 6),
            'g2': Pawn('BLACK', 7),
            'h2': Pawn('BLACK', 8)
        }
        self.squares.update(black_pawns)

        # Add White Pawns on row 7
        white_pawns = {
            'a7': Pawn('WHITE', 1),
            'b7': Pawn('WHITE', 2),
            'c7': Pawn('WHITE', 3),
            'd7': Pawn('WHITE', 4),
            'e7': Pawn('WHITE', 5),
            'f7': Pawn('WHITE', 6),
            'g7': Pawn('WHITE', 7),
            'h7': Pawn('WHITE', 8)
        }
        self.squares.update(white_pawns)

        # Set initial positions and board for each piece
        for square, piece in self.squares.items():
            if piece is not None:
                piece.set_initial_position(square)
                piece.define_board(self)

    def print_board(self):
        # Loop over each row from 8 to 1
        for row in range(8, 0, -1):
            current_row = []
            for col in range(ord('a'), ord('i')):
                square_name = f"{chr(col)}{row}"
                piece = self.squares[square_name]
                current_row.append(str(piece) if piece else None)
            print(current_row)

    def find_piece(self, symbol: str, identifier: int, color: str):
        """Finds and returns a list of pieces that match the given symbol, identifier, and color."""
        return [
            piece for square, piece in self.squares.items()
            if piece is not None and
               piece.symbol == symbol and
               piece.identifier == identifier and
               piece.color == color
        ]

    def get_piece(self, square):
        """Returns the piece that is on a specific square."""
        return self.squares[square]

    def is_square_empty(self, square):
        """Returns True if the square is empty, False otherwise."""
        return self.get_piece(square) is None

    def kill_piece(self, square):
        """Kills the piece on the specified square."""
        piece = self.get_piece(square)
        if piece is not None:
            piece.die()
            self.squares[square] = None

    def save_board(self, filename='board.txt'):
        """Save the current board state to a file."""
        with open(filename, 'a') as file:
            file.write(json.dumps({k: str(v) for k, v in self.squares.items() if v is not None}) + '\n')

    @staticmethod
    def load_board(filename='board.txt'):
        """Load board states from a file using a generator."""
        with open(filename, 'r') as file:
            for line in file:
                yield json.loads(line)

    def print_saved_board(self, board_state):
        """Print a saved board state."""
        for row in range(8, 0, -1):
            current_row = []
            for col in range(ord('a'), ord('i')):
                square_name = f"{chr(col)}{row}"
                piece = board_state.get(square_name)
                current_row.append(piece)
            print(current_row)
