#!/usr/bin/python
# -*- coding: utf-8 -*-


def print_board(board):
    '''Prints the board'''

    boardString = ''
    for i in range(9):
        for j in range(9):
            boardString += str(board[i][j]) + ' '
            if (j + 1) % 3 == 0 and j != 0 and j + 1 != 9:
                boardString += '| '

            if j == 8:
                boardString += '\n'

            if j == 8 and (i + 1) % 3 == 0 and i + 1 != 9:
                boardString += '- - - - - - - - - - - \n'
    print(boardString)


def find_empty(board):
    '''Finds an empty cell and returns its position as a tuple'''
    # Returns None if all cells are filled
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)


def valid_pose(board, pos, num):
    '''Tells whether num is valid in that cell or not, returns True or Flase'''

    for i in range(9):
        # Check in row
        if board[i][pos[1]] == num and (i, pos[1]) != pos:  
            return False

    for j in range(9):
        # Check in column
        if board[pos[0]][j] == num and (pos[0], j) != pos:  
            return False

    # Now check in 3x3 squares
    _i = pos[0] - pos[0] % 3  
    _j = pos[1] - pos[1] % 3
    for i in range(3):
        for j in range(3):  
            if board[_i + i][_j + j] == num and (_i + i,
                    _j + j) != pos:
                return False
    return True


def solve(board):
    '''Solves sudoku using backtracking algorithm'''

    empty = find_empty(board)
    if not empty:  
        # If all cells are filled, return True
        # Check is empty places are left on board
        return True

    for nums in range(9):
        if valid_pose(board, empty, nums + 1):
            # If position is valid, enter the number there
            board[empty[0]][empty[1]] = nums + 1

            if solve(board):  
                return True
            # If the board is not satisfying the requirements based on
            # number entered, it resets that position to 0
            board[empty[0]][empty[1]] = 0  
    return False


if __name__ == '__main__':
    board =  [
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 8, 0, 0, 0, 7, 0, 9, 0],
        [6, 0, 2, 0, 0, 0, 5, 0, 0],
        [0, 7, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 4, 0],
        [0, 0, 5, 0, 0, 0, 6, 0, 3],
        [0, 9, 0, 4, 0, 0, 0, 7, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 0]
    ]
    # print(valid_pose(board,pos=(1,1),num=8))
    # print(valid_pose(board,pos=(1,1),num=5))
    # print(valid_pose(board,pos=(0,0),num=6))
    # print(valid_pose(board,pos=(1,1),num=2))
    #--------------------------------------------valid_pose---works fine---checked----
    print_board(board)
    print("=====================")
    print("Solving the board, please wait...")
    print("=====================")
    solve(board)
    print_board(board)
    print("=====================")
