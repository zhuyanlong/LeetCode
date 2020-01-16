class Solution:
    def uniquePaths(self, m, n):
        if m==1 and n==1:
            return 1
        elif m==1 and n>1:
            return 1
        elif m>1 and n==1:
            return 1
        else:
            lst=[[0 for i in range(n)] for i in range(m)]
            for i in range(n):
                lst[0][i]=1
            for i in range(m):
                lst[i][0]=1
            for i in range(1,m):
                for j in range(1,n):
                    lst[i][j]=lst[i-1][j]+lst[i][j-1]
            # print(lst)
            return lst[m-1][n-1]

def main():
    m=7
    n=3
    s=Solution
    print(s.uniquePaths(None,m,n))
main()

