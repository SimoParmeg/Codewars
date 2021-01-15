#PRIMA SOLUZIONE
# def validSolution(board):
#     # rows & columns check
#     for row in range(len(board)):
#         row_sum = 0
#         col_sum = 0
#         for col in range(len(board)):
#             #vertical check
#             col_sum += board[col][row]
#             #horizontal check
#             row_sum += board[row][col]
#             #no zeros check
#             if board[row][col] == 0:
#                 return False
#         #sudoku check
#         if col_sum != 45 or row_sum != 45:
#             return False
#     # 3x3 square check
#     for row in range(3):
#         for col in range(3):
#             grid_sum = 0
#             for row2 in range(3):
#                 for col2 in range(3):
#                     grid_sum += board[row*3 + row2][col*3 + col2]
#             if grid_sum != 45:
#                 return False
#     return True

#SECONDA SOLUZIONE
def valid_solution(board):
    row = validate_rows(board)
    cols = validate_cols(board)
    boxes = validate_boxes(board)

    return row and cols and boxes


def validate_rows(board):
    for row in range(len(board)):
        row_sum = 0
        for col in range(len(board)):
            # no zeros check
            if board[row][col] == 0:
                return False
            row_sum += board[row][col]
        print(f"row_sum = {row_sum}")
        if row_sum != 45:
            return False


def validate_cols(board):
    for row in range(len(board)):
        col_sum = 0
        for col in range(len(board)):
            col_sum += board[col][row]
        print(f"col_sum = {col_sum}")
        if col_sum != 45:
            return False


def validate_boxes(board):
    for row in range(3):
        for col in range(3):
            grid_sum = 0
            for row2 in range(3):
                for col2 in range(3):
                    grid_sum += board[row * 3 + row2][col * 3 + col2]
            print(f"grid_sum = {grid_sum}")
            # sudoku check
            if grid_sum != 45:
                return False
    return True

print(valid_solution([
  [5, 3, 4, 6, 7, 8, 9, 1, 2],
  [6, 7, 2, 1, 9, 5, 3, 4, 8],
  [1, 9, 8, 3, 4, 2, 5, 6, 7],
  [8, 5, 9, 7, 6, 1, 4, 2, 3],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],
  [9, 6, 1, 5, 3, 7, 2, 8, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 4, 5, 2, 8, 6, 1, 7, 9]
])); # TRUE

print(valid_solution([
  [5, 3, 4, 6, 7, 8, 9, 1, 2],
  [6, 7, 2, 1, 9, 0, 3, 4, 8],
  [1, 0, 0, 3, 4, 2, 5, 6, 0],
  [8, 5, 9, 7, 6, 1, 0, 2, 0],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],
  [9, 0, 1, 5, 3, 7, 2, 1, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 0, 0, 4, 8, 1, 1, 7, 9]
])) #FALSE