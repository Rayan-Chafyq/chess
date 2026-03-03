from board import Board

# Create a Board object
board = Board()

# Print the squares dictionary
for square, piece in board.squares.items():
    print(f"{square}: {piece}")
