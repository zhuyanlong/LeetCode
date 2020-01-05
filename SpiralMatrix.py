#这道题目的核心是，他的遍历方向是确定的，唯一不确定的仅仅是从那个地方开始遍历
#方向是right-down-left-up
class Solution:
    def spiralOrder(self, matrix):
        if matrix==None or len(matrix)==0:
            return []
        up=0
        left=0
        right=len(matrix[0])-1
        down=len(matrix)-1
        direct=0 #方向指示量
        res=[]
        while True:
            #向右遍历
            if direct==0:
                for i in range(left,right+1):
                    res.append(matrix[up][i])
                up+=1
            #向下遍历
            if direct==1:
                for i in range(up,down+1):
                    res.append(matrix[i][right])
                right-=1
            #向左遍历
            if direct==2:
                for i in range(right,left-1,-1):
                    res.append(matrix[down][i])
                down-=1
            #向上遍历
            if direct==3:
                for i in range(down,up-1,-1):
                    res.append(matrix[i][left])
                left+=1
            # print(direct)
            direct=(direct+1)%4
            if down<up or left>right:
                return res

def main():
    matrix=[]
    s=Solution
    print(s.spiralOrder(None,matrix))

main()