#Created by Tristan Crocker
import tkinter
import numpy as np
import random

rootwindow = tkinter.Tk()
rootwindow.title('Test')
rootwindow.configure(bg = 'black')
rootwindow.resizable(0,0)

board = np.array([[3, 0, 6, 5, 0, 8, 4, 0, 0],[5, 2, 0, 0, 0, 0, 0, 0, 0],[0, 8, 7, 0, 0, 0, 0, 3, 1],[0, 0, 3, 0, 1, 0, 0, 8, 0],[9, 0, 0, 8, 6, 3, 0, 0, 5],[0, 5, 0, 0, 9, 0, 6, 0, 0],[1, 3, 0, 0, 0, 0, 2, 5, 0],[0, 0, 0, 0, 0, 0, 0, 7, 4],[0, 0, 5, 2, 0, 6, 3, 0, 0]]).reshape(9,9)
# board = np.array([[3,0,0],[0,0,0],[0,2,0]]).reshape(3,3)

rows = []
buttons = []
stop = False

def guigrid():
    global buttons
    global rows
    rows = []
    i = -1
    for row in board:
        j = -1
        i = i + 1
        cols = []
        for col in row:
            j = j + 1
            label = tkinter.Label(rootwindow, text = col, height = 5, width = 10, borderwidth = 0)
            label.grid(row = i, column = j, padx = 1, pady = 1)
            cols.append(label) 
        rows.append(cols)
        button = tkinter.Button(rootwindow, text = 'START', bg = 'red', width = 5, command = stop)
        button.grid(row = i + 1, columnspan = 30)
 


def stop():
    global stop
    stop = True
    return stop

guigrid()


def refresh(): 
    while True:
        rootwindow.update()
        rootwindow.after(100)
        if stop == True:
            break

refresh()
stop = False


def check_valid(board, value, index):

    #Check down column
    for row in range(board.shape[0]):
        if value == board[row][index[1]]:
            return False
    

    #Check across row
    for col in range(board.shape[1]):
        if value == board[index[0]][col]:
            return False
    

    # check in 3x3 grid
    if board.shape[0] == 9 and board.shape[1] == 9:
        #Only do this check for 9x9 boards
        if index[0] <= 2 and index[1] <=2:
            for row in range(0,3):
                for col in range(0,3):
                    if board[row][col] == value:
                        return False

        elif (index[0] > 2 and index[0] <=5) and index[1] <=2:
            for row in range(3,6):
                for col in range(0,3):
                    if board[row][col] == value:
                        return False

        elif (index[0] > 5 and index[0] <=8) and index[1] <=2:
            for row in range(6,9):
                for col in range(0,3):
                    if board[row][col] == value:
                        return False

        elif index[0] <= 2 and (index[1] >2 and index[1] <= 5):
            for row in range(0,3):
                for col in range(3,6):
                    if board[row][col] == value:
                        return False

        elif index[0] <= 2 and (index[1] >5 and index[1] <= 8):
            for row in range(0,3):
                for col in range(6,9):
                    if board[row][col] == value:
                        return False

        elif (index[0] > 2 and index[0]<=5 ) and (index[1] >2 and index[1] <= 5):
            for row in range(3,6):
                for col in range(3,6):
                    if board[row][col] == value:
                        return False
        
        elif (index[0] > 2 and index[0]<=5 ) and (index[1] >5 and index[1] <= 8):
            for row in range(3,6):
                for col in range(6,9):
                    if board[row][col] == value:
                        return False

        elif (index[0] > 5 and index[0]<=8 ) and (index[1] >2 and index[1] <= 5):
            for row in range(6,9):
                for col in range(3,6):
                    if board[row][col] == value:
                        return False
        
        elif (index[0] > 5 and index[0]<=8 ) and (index[1] >5 and index[1] <= 8):
            for row in range(6,9):
                for col in range(6,9):
                    if board[row][col] == value:
                        return False
    return True


def solve(board):
    #Check for empty blocks
    empty = False

    for row in range(board.shape[0]):
        if empty == True:
            break
        for col in range(board.shape[1]):
            if board[row][col] == 0:
                empty = True
                index = [row,col]
                break
                
    if empty == False:
        '''This check if there are any more blocks, in the lowest level solve(board) condition, 
           on the last solution if a number picked is valid then it'll enter into a new solve(board) condition, 
           but index will be none so it'll return true, causing all upper solve(board) conditions to return true until the outter solve(board),
           therefore all conditions will be true and it'll be solved'''
        return True

    for n in range(1, board.shape[0] + 1):
        if check_valid(board, n, index):
            board[index[0]][index[1]] = n
            rows[index[0]][index[1]].configure(text = n)
            rootwindow.update()
            rootwindow.after(10)


            if solve(board):
                #Backtracking
                '''This will return true if the final solution(lowest level solve(board) condition) returns true
                   as it'll have a domino affect causing all upper level solve(board) conditions to be true
                   and therefore exiting the function.'''
                '''If no solution for a specific block, it'll return false causing the upper level solve(board) condition to be false and to not perform the action 'return true', 
                   it will then set the block to 0 and try the next number in the loop for that block. This is repeated for each block until a correct combination if found.'''
                return True

            
            board[index[0]][index[1]] = 0
            
    return False


if __name__ == '__main__':
    solve(board)
    refresh()