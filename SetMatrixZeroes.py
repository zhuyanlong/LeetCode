#最笨的办法是从头到尾扫描，扫到一个0，就把行和列都置成0，这样子最坏时间复杂度是O(n^2)，我觉得可以先试一下这种方法
#模拟了下，几乎不可行，时间复杂度实在太高了
#不过还是先试着用这种方式写一下，理解下这道题目的意思
# class Solution:
#     def setZeroes(self, matrix):
#         m=len(matrix)
#         n=len(matrix[0])
#         row=[False for i in range(m)]
#         col=[False for i in range(n)]
#         for i in range(m):
#             for j in range(n):
#                 if matrix[i][j]==0:
#                     row[i]=True
#                     col[j]=True
#         for i in range(m):
#             for j in range(n):
#                 if row[i] or col[j]:
#                     matrix[i][j]=0
#         print(matrix)

#类似于完全遍历，但这是一种更精细的操作，只对需要修改的数据进行修改，跳过不需要修改的数据，算法很精妙，但感觉不是很大众化
class Solution:
    def setZeroes(self, matrix):
        m=len(matrix)
        n=len(matrix[0])
        rows=[]
        cols=[]
        #这个对0的获取能不能再降低下复杂度
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    rows.append(i)
                    cols.append(j)
        for i in rows:
            matrix[i]=[0]*len(matrix[i])
        for row in matrix:
            for j in cols:
                row[j]=0
        print(matrix)

def main():
    matrix=[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
    s=Solution
    s.setZeroes(None,matrix)

main()