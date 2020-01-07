class Solution:
    def generateMatrix(self, n):
        if n==0:
            return []
        matrix=[]
        for i in range(n):
            tmp=[]
            for j in range(n):
                tmp.append(0)
            matrix.append(tmp)
        # print(matrix)
        up=0
        left=0
        right=n-1
        down=n-1
        direct=0
        count=1
        while True:
            
            if direct==0:
                for i in range(left,right+1):
                    matrix[up][i]=count
                    count+=1
                up+=1
            if direct==1:
                for i in range(up,down+1):
                    matrix[i][right]=count
                    count+=1
                right-=1
            if direct==2:
                for i in range(right,left-1,-1):
                    matrix[down][i]=count
                    count+=1
                down-=1
            if direct==3:
                for i in range(down,up-1,-1):
                    matrix[i][left]=count
                    count+=1
                left+=1
            if up>down or left>right:
                print(matrix)
                return matrix
            direct=(direct+1)%4
        

def main():
    n=5
    s=Solution
    s.generateMatrix(None, n)

main()
