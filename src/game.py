from random import choice

from board import Board

RED = 1
BLUE = -1
DRAW = 0

class Game():
    def __init__(self, START_PLAYER = RED):
        self.board = Board()
        self.player = START_PLAYER
        self.turn = 0
        self.result = None

        self.set_order = []        

        self.START_PLAYER = START_PLAYER

    
    def next_state(self, action):
        self.board.set_stone(*action)

    def random_action(self):
        return choice(self.board.placable_index())

    def is_finished(self):
        if self.board.placable_index() == []:
            return True

        self.result = self.board.judge_winner()
        return self.result == RED or self.result == BLUE

    def is_first_player(self):
        return self.player == self.START_PLAYER

    def next_player(self):
        return BLUE if self.player == RED else RED
    
    def player_to_str(self, player):
        if player == RED:
            return "RED"
        if player == BLUE:
            return "BLUE"
