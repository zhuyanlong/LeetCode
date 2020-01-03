# class Solution:
#     def isValidSudoku(self, board):
#         def isValid(i,j,tmp):
#             for k in range(9):
#                 if tmp==board[i][k]:
#                     return False
#             for k in range(9):
#                 if tmp==board[k][j]:
#                     return False
#             for k in range(3):
#                 for m in range(3):
#                     if board[int(i/3)*3+k][int(j/3)*3+m]==tmp:
#                         return False

#             return True

#         for i in range(9):
#             for j in range(9):
#                 if board[i][j]=='.':
#                     continue
#                 else:
#                     tmp=board[i][j]
#                     board[i][j]='D'
#                     if isValid(i,j,tmp)==False:
#                         return False
#                     else:
#                         board[i][j]=tmp
#         return True

#官方解
#大概就是利用字典实现快速查找
class Solution:
    def isValidSudoku(self, board):
        rows = [{} for i in range(9)]
        columns = [{} for i in range(9)]

        #这个是用来做什么的？
        boxes = [{} for i in range(9)]

        # validate a board
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    num = int(num)
                    box_index = (i // 3 ) * 3 + j // 3
                    
                    # keep the current cell value
                    rows[i][num] = rows[i].get(num, 0) + 1
                    columns[j][num] = columns[j].get(num, 0) + 1
                    boxes[box_index][num] = boxes[box_index].get(num, 0) + 1
                    
                    # check if this value has been already seen before
                    if rows[i][num] > 1 or columns[j][num] > 1 or boxes[box_index][num] > 1:
                        return False         
        return True

def main():
    board=[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
    s=Solution
    print(s.isValidSudoku(None,board))

main()