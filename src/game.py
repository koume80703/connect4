from board import Board

RED = 1
BLUE = -1
DRAW = 0

class Game():
    def __init__(self, START_PLAYER = RED):
        self.board = Board()
        self.player = self.START_PLAYER
        self.turn = 0
        self.result = None

        self.set_order = []
        
        self.draw = False

        self.START_PLAYER = START_PLAYER
    
    def player_to_str(self, player):
        if player == RED:
            return "RED"
        if player == BLUE:
            return "BLUE"