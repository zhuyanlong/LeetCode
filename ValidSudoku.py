#data structure dict()
# class Solution:
#     def isValidSudoku(self, board):
#         rows = [{} for i in range(9)]
#         columns = [{} for i in range(9)]
#         boxes = [{} for i in range(9)]

#         # validate a board
#         for i in range(9):
#             for j in range(9):
#                 num = board[i][j]
#                 if num != '.':
#                     num = int(num)
#                     box_index = (i // 3 ) * 3 + j // 3
                    
#                     # keep the current cell value
#                     rows[i][num] = rows[i].get(num, 0) + 1
#                     columns[j][num] = columns[j].get(num, 0) + 1
#                     boxes[box_index][num] = boxes[box_index].get(num, 0) + 1
                    
#                     # check if this value has been already seen before
#                     if rows[i][num] > 1 or columns[j][num] > 1 or boxes[box_index][num] > 1:
#                         return False         
#         return True


#data structure: set()
class Solution:
    def isValidSudoku(self, board):
        rows=[set() for i in range(9)]
        columns=[set() for i in range(9)]
        boxs=[set() for i in range(9)]
        for i in range(9):
            for j in range(9):
                num=board[i][j]
                boxindex=int(i//3*3+j//3)
                if num!='.':
                    num=int(num)
                    if num in rows[i]:
                        return False
                    else:
                        rows[i].add(num)
                    if num in columns[j]:
                        return False
                    else:
                        columns[j].add(num)
                    if num in boxs[boxindex]:
                        return False
                    else:
                        boxs[boxindex].add(num)
        print(columns)
        return True

def main():
#     board=[
#   ["8","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ]
    board=[
    [".",".","4",".",".",".","6","3","."],
    [".",".",".",".",".",".",".",".","."],
    ["5",".",".",".",".",".",".","9","."],
    [".",".",".","5","6",".",".",".","."],
    ["4",".","3",".",".",".",".",".","1"],
    [".",".",".","7",".",".",".",".","."],
    [".",".",".","5",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."]]

    s=Solution
    print(s.isValidSudoku(None,board))

main()
