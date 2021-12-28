from board import Board
from game import Game
from mcts.mcts import MCTS
from node import Node


def main():
    game = Game()
    
    i = 0
    while not game.is_finished():
        if game.is_first_player():
            root_node = Node(game, expand_base = 20)

            MCTS.train(root_node = root_node, simulation=100)
            action = MCTS.select_action(root_node)

            game.next_state(action)
        else:
            action = game.random_action()
            game.next_state(action)
    
    return

if __name__ == "__main__":
    main()
