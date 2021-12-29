import sys

import numpy as np

EMPTY = 0
WALL = 2
RED = -1
BLUE = 1

class Board():
    ROW_SIZE = 7+2 #横方向の大きさ
    COL_SIZE = 6+2 #縦方向の大きさ

    def __init__(self):
        self.board = np.zeros((self.ROW_SIZE, self.COL_SIZE), dtype = int)

        #外周を壁とする
        self.board[0, :] = WALL
        self.board[:, 0] = WALL
        self.board[-1, :] = WALL
        self.board[:, -1] = WALL

    def set_stone(self, x : int, y : int, player : int):
        if self.board[y, x] != EMPTY:
            return False
        
        self.board[y, x] = player
        return True

    def placable_index(self):
        placable = []
        for x in range(1, self.ROW_SIZE-1):
            for y in range(1, self.COL_SIZE-1)[::-1]:
                if self.board[y, x] == EMPTY:
                    placable.append((x, y))
                    break

        if len(placable) > self.ROW_SIZE-2:
            print("error: out of index in <placable_index>")
            sys.exit()

        return placable

    def judge_winner(self):
        for y in range(1, self.COL_SIZE-1)[::-1]:
            for x in range(1, self.ROW_SIZE-1):
                board_type = self.board[y, x]
                if board_type == EMPTY:
                    continue
                if board_type == RED or board_type == BLUE:
                    if self.judge_consecutive_stone(x, y, board_type):
                        return board_type
                        
    def judge_consecutive_stone(self, x, y, player):
        PREV, NEXT = -1, 1
        ROW_DIRECTION = [PREV, 0, NEXT]
        COL_DIRECTION = [0, NEXT]        
        
        for dy in COL_DIRECTION:
            for dx in ROW_DIRECTION:
                if dx == 0 and dy == 0:
                    continue
                count_stone = 1
                depth = 0
                while(True):
                    depth += 1

                    rx = x + (dx * depth)
                    ry = y + (dy * depth)

                    board_type = self.board[ry, rx]

                    if board_type == WALL or board_type == EMPTY:
                        break
                    elif board_type != player:
                        break

                    count_stone += 1
                    if count_stone == 4:
                        return True
        else:
            return False

    def show_board(self):
        print("--" * 20)
        for y in range(self.COL_SIZE):
            for x in range(self.ROW_SIZE):
                if self.board[x, y] == 0:
                    print("* ", end = "")
                elif self.board[x, y] == 2:
                    print(". ", end = "")
                elif self.board[x, y] == -1:
                    print("R ", end = "")
                elif self.board[x, y] == 1:
                    print("B ", end = "")
            else:
                print("\n", end = "")
        print("--" * 20)

    def get_board(self):
        return self.board
