#place 8 queens on an 8x8 chessboard without any being able to attack each other
#grid layout using indexing from 0
#origin (0,0) at top left
BOARD_SIZE = 12
board = [['x' for i in range(BOARD_SIZE)] for i in range(BOARD_SIZE)]
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
    # Get dynamic board size
    size = len(board)
    
    # Create dynamic layout string using join
    layout = '|' + '|'.join([' {} '] * size) + '|'
    border = '_' * (len(layout.format(*['x']*size)))
    
    for i in range(size):
        print(border)
        # Pass entire row to format
        row_display = [board[row][i] for row in range(size)]
        print(layout.format(*row_display))
        
    print(border)
  
  
    
# Start solving
solve(0, board, queens)

    
  
