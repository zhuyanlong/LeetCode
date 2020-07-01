class Solution:
    def minimumTotal(self, triangle):
        result=[0 for i in range(len(triangle))]
        if len(triangle)==0:
            return 0
        result[0]=triangle[0][0]
        for i in range(1,len(triangle)):
            for j in range(len(triangle[i])-1,-1,-1):
                if j==len(triangle[i])-1:
                    result[j]=result[j-1]+triangle[i][j]
                elif j==0:
                    result[j]=result[j]+triangle[i][j]
                else:
                    result[j]=min(result[j-1],result[j])+triangle[i][j]
        # print(result)
        return min(result)
        

def main():
    s=Solution()
    triangle=[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
    s.minimumTotal(triangle)
main()

