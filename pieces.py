class Piece:
    def __init__(self, colour:bool):
        self.colour = colour

class Pawn(Piece):
    def __init__(self, colour: bool):
        super().__init__(colour)

    def __str__(self) -> str:
        if self.colour==True:
            return 'P'
        else:
            return 'p'

class Rook(Piece):
    def __init__(self, colour: bool):
        super().__init__(colour)

    def __str__(self) -> str:
        if self.colour==True:
            return 'R'
        else:
            return 'r'

class Bishop(Piece):
    def __init__(self, colour: bool):
        super().__init__(colour)

    def __str__(self) -> str:
        if self.colour==True:
            return 'B'
        else:
            return 'b'

class Knight(Piece):
    def __init__(self, colour: bool):
        super().__init__(colour)

    def __str__(self) -> str:
        if self.colour==True:
            return 'N'
        else:
            return 'n'

class Queen(Piece):
    def __init__(self, colour: bool):
        super().__init__(colour)

    def __str__(self) -> str:
        if self.colour==True:
            return 'Q'
        else:
            return 'q'

class King(Piece):
    def __init__(self, colour: bool):
        super().__init__(colour)

    def __str__(self) -> str:
        if self.colour==True:
            return 'K'
        else:
            return 'k'

        