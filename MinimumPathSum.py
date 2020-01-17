class Solution:
    def minPathSum(self, grid):
        m=len(grid)
        n=len(grid[0])
        lst=[[0 for i in range(n)] for i in range(m)]
        lst[0][0]=grid[0][0]
        for i in range(1, n):
            lst[0][i]=lst[0][i-1]+grid[0][i]
        for j in range(1, m):
            lst[j][0]=lst[j-1][0]+grid[j][0]
        for i in range(1, m):
            for j in range(1, n):
                lst[i][j]=min(lst[i-1][j],lst[i][j-1])+grid[i][j]
        # print(lst)
        return lst[m-1][n-1]

def main():
    s=Solution
    grid=[
    [1,3,1],
    [1,5,1],
    [4,2,1]
]
    print(s.minPathSum(None,grid))

main()
