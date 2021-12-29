from node import Node
from mcts.util.argmax import argmax

class MCTS:
    @classmethod
    def train(cls, root_node, simulation):
        root_node.expand()
        for _ in range(simulation):
            root_node.evaluate()

    @classmethod
    def select_action(cls, root_node):
        placable = root_node.game.board.placable_index()
        visit_list = [child.n for child in root_node.children]
        return placable[argmax(visit_list)]