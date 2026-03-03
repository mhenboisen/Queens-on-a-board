#place 8 queens on an 8x8 chessboard without any being able to attack each other
#grid layout using indexing from 0
#origin (0,0) at top left
BOARD_SIZE = 8
board = [['x' for i in range(BOARD_SIZE)] for i in range(BOARD_SIZE)]
layout = '| {} | {} | {} | {} | {} | {} | {} | {} |'
border = '_' * 33
queens = []

def placeQueen(row,column,board):
  board[row][column] = 'Q'
  queens.append((row,column))
  
def removeQueen(row,column,board):
  board[row][column] = 'x'
  queens.remove((row,column))

def checkAttacks(queens):
  for i, q1 in enumerate(queens):
    for q2 in queens[i+1:]:  # Only check later queens
      row1, col1 = q1
      row2, col2 = q2
      
      # Same row, column, or diagonal?
      if (row1 == row2 or 
        col1 == col2 or 
        abs(row1 - row2) == abs(col1 - col2)):
        return True  # Attack detected
  return False

def solve(row, board, queens):
    if row == BOARD_SIZE:  # All queens placed
        showBoard(board)
        return True
    
    for col in range(BOARD_SIZE):
        placeQueen(row, col, board)
        if not checkAttacks(queens):
            if solve(row + 1, board, queens):  # Recurse
                return True
        removeQueen(row, col, board)  # Backtrack
    
    return False  # No solution from this path

def showBoard(board):
  for i in range(8):
    print(border)
    print(layout.format(board[0][i],board[1][i],board[2][i],board[3][i],board[4][i],board[5][i],board[6][i], board[7][i]))
  print(border + '\n')
  
  
    
# Start solving
solve(0, board, queens)

    
  
