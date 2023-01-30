import pieces

class Board():
    def __init__(self):
        
        # Uses list comprehension to generate an 8x8 matrix

        self.board = [[[] for i in range(8)] for i in range(8)]

        # Set up black pieces, then white pieces

        for square in self.board[1]:
            square = pieces.Pawn(colour=False)

        self.board[0][0] = pieces.Rook(colour=False)
        self.board[0][1] = pieces.Knight(colour=False)
        self.board[0][2] = pieces.Bishop(colour=False)
        self.board[0][3] = pieces.Queen(colour=False)
        self.board[0][4] = pieces.King(colour=False)
        self.board[0][5] = pieces.Bishop(colour=False)
        self.board[0][6] = pieces.Knight(colour=False)
        self.board[0][7] = pieces.Rook(colour=False)

        for square in self.board[1]:
            square = pieces.Pawn(colour=True)

        self.board[7][0] = pieces.Rook(colour=True)
        self.board[7][1] = pieces.Knight(colour=True)
        self.board[7][2] = pieces.Bishop(colour=True)
        self.board[7][3] = pieces.Queen(colour=True)
        self.board[7][4] = pieces.King(colour=True)
        self.board[7][5] = pieces.Bishop(colour=True)
        self.board[7][6] = pieces.Knight(colour=True)
        self.board[7][7] = pieces.Rook(colour=True)


    def print_board(self):
        row = '+---+---+---+---+---+---+---+---+\n'
        #print(self.board)

        for rank in self.board:
            print(row)
            for file in rank:
                if file == []:
                    print(' ',' | ',end='')
                else:
                    print(file.__str__(),' | ',end='')

            print('\n')
            