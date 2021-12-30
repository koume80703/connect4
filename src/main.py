from game import Game


RED = -1
BLUE = 1
DRAW = 0

START_PLAYER = RED


def play_connect4():
    game = Game()

    while not game.is_finished():
        if game.is_first_player():
            action = game.mcts_player(RED)
            game.next_state(action)
        else:
            action = game.mcts_player(BLUE, expand_base=100, simulation=1000)
            game.next_state(action)

    game.board.show_board()
    game.show_result()

    return game.result


def main():
    game_num = 100
    n_win, n_lose, n_draw = 0, 0, 0
    for i in range(game_num):
        print(f"<play {i}>")
        result = play_connect4()
        if result == RED:
            n_win += 1
        elif result == BLUE:
            n_lose += 1
        elif result == DRAW:
            n_draw += 1
        else:
            print("result was illegal value")

    print(f"win: {n_win}, lose: {n_lose}, draw: {n_draw}")


if __name__ == "__main__":
    main()
