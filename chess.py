import board
import pieces

class Chess():
    def __init__(self) -> None:
        self.board = board.Board()


chess = Chess()
chess.board.print_board()