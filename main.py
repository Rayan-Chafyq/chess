from board import Board

def main():
    board = Board()
    board.setup_board()
    board.print_board()

    # Example of moving a piece
    pawn = board.get_piece('a2')
    pawn.move()

    # Example of saving the board state
    board.save_board()

    # Example of loading and printing a saved board state
    for state in Board.load_board():
        board.print_saved_board(state)

if __name__ == "__main__":
    main()

