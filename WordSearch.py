#正常回溯，空间占优，但是时间复杂度比较高
class Solution:
    def exist(self, board, word):
        if len(board)==0:
            return False
        m=len(board)
        n=len(board[0])
        tmp={}
        for i in range(m):
            for j in range(n):
                if board[i][j] not in tmp:
                    tmp[board[i][j]]=1
                else:
                    tmp[board[i][j]]+=1
        for i in word:
            if i in tmp:
                tmp[i]-=1
                if tmp[i]==0:
                    tmp.pop(i)
            else:
                return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0]:
                    result=[]
                    stack=[(i,j,len(result))]
                    while stack:
                        top=stack.pop()
                        # print("top",top)
                        #保持同层
                        while top[2]!=len(result):
                            result.pop()
                        result.append((top[0],top[1]))
                        # print("result",result)
                        dirs=[[0,-1],[0,1],[-1,0],[1,0]]
                        for d in dirs:
                            x=d[0]+top[0]
                            y=d[1]+top[1]
                            if len(result)==len(word):
                                return True
                            if x>=0 and y>=0 and x<len(board) and y<len(board[0]):
                                if board[x][y]==word[len(result)] and (x,y) not in result:
                                    stack.append((x,y,len(result)))
                        # print("stack",stack)
        return False



def main():
    board =[
    ['A','B','C','E'],
    ['S','F','C','S'],
    ['A','D','E','E']
]
    s=Solution
    word="ABCB"
    print(s.exist(s,board,word))
main()