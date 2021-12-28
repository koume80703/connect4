from copy import deepcopy
from mcts.util.argmax import argmax
from mcts.util.ucb1 import ucb1

class Node():
    def __init__(self, game, expand_base = 20):
        self.game = game
        self.w = 0
        self.n = 0
        self.expand_base = expand_base
        self.children = None

    def evaluate(self):
        if self.game.is_finished():
            value = 0
            if self.game.is_win():
                value = 1
            elif self.game.is_lose():
                value = -1
            
            self.w += value
            self.n += 1

            return value

        if self.children is None:
            value = Node.playout(deepcopy(self.game))
            self.w += value
            self.n += 1

            if self.n == self.expand_base:
                self.expand()
            
            return value
        else:
            value = self.next_child_based_ucb().evaluate()
            self.w += value
            self.n += 1

            return value

    def expand(self):
        if self.game.board.placable_index() == []:
            return
        self.children = [Node(deepcopy(self.game).next_state(action), self.expand_base) for action in self.game.board.placable_index()]

    def next_child_based_ucb(self):
        for child in self.children:
            if child.n == 0:
                return child

        sum_n = sum([child.n for child in self.children])
        ucb1_values = [ucb1(sum_n, child.n, child.w) for child in self.children]

        return self.children[argmax(ucb1_values)]

    def playout(cls, game):
        if game.is_finished():
            if game.is_win():
                return 1
            elif game.is_lose():
                return -1
            else:
                return 0

        return Node.playout(game.next_state(game.random_action()))