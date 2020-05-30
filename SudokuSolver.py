class Solution:
    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        #决定改下判断函数，用最简单的判断函数，否则整体上做起来很麻烦
        def isValid(x,y,z):
            for i in range(9):
                if z==board[x][i]:
                    # print("1")
                    return False
                if z==board[i][y]:
                    # print('2')
                    return False
            for i in range(3):
                for j in range(3):
                    # print(board[x//3*3+i][y//3*3+j])
                    if z==board[x//3*3+i][y//3*3+j]:
                        # print("3")
                        return False
            return True

        def isFull():
            for i in range(len(board)):
                if board[i].count('.')!=0:
                    return False
            return True

        def init():
            index={}
            k=0
            for i in range(9):
                for j in range(9):
                    num=board[i][j]
                    if num=='.':
                        index[k]=(i,j)
                        k+=1
            return index

        index=init()
        # print(index)
        result=[]
        stack=[]
        for k in "123456789":
            if isValid(index[0][0],index[0][1],k):
                stack.append((0,k))
        # print(stack)
        #result和board要始终保持一致
        while stack:
            top=stack.pop()
            while len(result)!=top[0]:
                t=len(result)-1
                result.pop()
                # print(index[t][0],index[t][1])
                board[index[t][0]][index[t][1]]='.'
            result.append(top[1])
            idx=len(result)
            board[index[idx-1][0]][index[idx-1][1]]=result[idx-1]
            # print(index[idx-1][0],index[idx-1][1])
            for k in "123456789":
                if idx==len(index):
                    break
                if isValid(index[idx][0],index[idx][1],k):
                    stack.append((idx,k))
            if isFull():
                print(board)
                return

def main():
    board=[
    ['5','3','.','.','7','.','.','.','.'],
    ['6','.','.','1','9','5','.','.','.'],
    ['.','9','8','.','.','.','.','6','.'],
    ['8','.','.','.','6','.','.','.','3'],
    ['4','.','.','8','.','3','.','.','1'],
    ['7','.','.','.','2','.','.','.','6'],
    ['.','6','.','.','.','.','2','8','.'],
    ['.','.','.','4','1','9','.','.','5'],
    ['.','.','.','.','8','.','.','7','9']]
    s=Solution
    s.solveSudoku(s,board)
    # print(board)

main()