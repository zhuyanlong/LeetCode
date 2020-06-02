class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m=len(obstacleGrid)
        if m!=0:
            n=len(obstacleGrid[0])
        else:
            n=0
        if m==1 and n==1 and obstacleGrid[0][0]==0:
            return 1
        if m==1 and n==1 and obstacleGrid[0][0]==1:
            return 0
        if m==1 and n>1:
            for i in range(n):
                if obstacleGrid[0][i]==1:
                    return 0
            return 1
        if m>1 and n==1:
            for i in range(m):
                if obstacleGrid[i][0]==1:
                    return 0
            return 1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j]==1:
                    obstacleGrid[i][j]=0
                else:
                    obstacleGrid[i][j]=1
        judge=1
        for i in range(m):
            if obstacleGrid[i][0]==0:
                judge=0
            obstacleGrid[i][0]=judge

        judge=1
        for i in range(n):
            if obstacleGrid[0][i]==0:
                judge=0
            obstacleGrid[0][i]=judge
        # print(obstacleGrid)

        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j]!=0:
                    obstacleGrid[i][j]=obstacleGrid[i-1][j]+obstacleGrid[i][j-1]
        # print(obstacleGrid)
        return obstacleGrid[m-1][n-1]

def main():
    # obstacleGrid=[
    #             [0,0,0],
    #             [0,1,0],
    #             [0,0,0]
    #             ]
    obstacleGrid=[[0,0,0,0,0,0],[1,0,1,0,1,0],[0,0,0,0,0,0],[0,0,0,1,0,0]]
    s=Solution
    print(s.uniquePathsWithObstacles(s,obstacleGrid))

main()