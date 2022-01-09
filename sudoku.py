#!/usr/bin/env python
# coding: utf-8

# In[28]:



def solve(board):
    """
    Solves a sudoku board using backtracking
    :parameters board: 2d list of integers
    :return: solution
    """
    find = find_empty(board)
    if find:
        row, col = find
    else:
        print_board(board)
        return True

    for i in range(1,10):
        if valid(board, (row, col), i):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False


def valid(board, pos, num):
    """
    Returns if the attempted move is valid
    :param board: 2d list of integers
    :param pos: (row, col) - tuple
    :param num: int
    :return: bool
    """

    # Check row
    for i in range(0, len(board)):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check Column
    for i in range(0, len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box

    box_x = pos[1]//3
    box_y = pos[0]//3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False

    return True


def find_empty(board):
    """
    finds an empty space in the board - empty space is denoted by zero
    :parameters board: partially complete board
    :return: (int, int) row col of empty space
    """

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)

    return None


def print_board(board):
    """
    prints the board
    :parameters board: 2d List of integers
    :return: None
    """
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - - - - - - - -")
        for j in range(len(board[0])):
            if j % 3 == 0:
                print(" | ",end="")

            if j == 8:
                print(board[i][j], " | ", end="\n")
            else:
                print(board[i][j], " ", end="")


# In[29]:


# input - initial sudoku is provided as 2d list of integers (9x9)

board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]


# In[30]:


solve(board)


# In[ ]:




