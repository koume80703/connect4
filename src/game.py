from random import choice
from typing import Tuple, Union

from board import Board
from mcts.mcts import MCTS
from node import Node


RED = -1
BLUE = 1
DRAW = 0


class Game():
    def __init__(self, START_PLAYER=RED):
        self.board = Board()
        self.player = START_PLAYER
        self.turn = 0
        self.result = None

        self.set_order = []

        self.START_PLAYER = START_PLAYER

    def next_state(self, action: Tuple[int, int]):
        self.board.set_stone(*action, self.player)

        self.set_order.append(action)

        self.turn += 1
        self.player = RED if self.player == BLUE else BLUE

    def random_action(self):
        return choice(self.board.placable_index())

    def is_finished(self):
        if self.board.placable_index() == []:
            self.result = DRAW
        else:
            self.result = self.board.judge_winner()
        return self.result is not None

    def is_win(self):
        return self.result == self.START_PLAYER

    def is_lose(self):
        return self.result == -self.START_PLAYER

    def is_draw(self):
        return self.result == DRAW

    def is_first_player(self):
        return self.player == self.START_PLAYER

    def next_player(self):
        return BLUE if self.player == RED else RED

    def mcts_player(self, expand_base: int = 20, simulation: int = 100):
        root_node = Node(self, expand_base=expand_base)
        MCTS.train(root_node=root_node, simulation=simulation)
        action = MCTS.select_action(root_node)

        return action

    def random_player(self):
        return self.random_action()

    def result_to_str(self, result: Union[None, int]):
        if result == RED:
            return "RED"
        if result == BLUE:
            return "BLUE"
        if result == DRAW:
            return "DRAW"

    def show_result(self):
        print(f"winner: {self.result_to_str(self.result)}")
