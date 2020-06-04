# class Solution:
#     def searchMatrix(self, matrix, target):
#         m=len(matrix)
#         if m!=0:
#             n=len(matrix[0])
#         else:
#             n=0
#         tmp=[]
#         for i in range(m):
#             tmp+=matrix[i]
#         i=0
#         j=m*n-1
#         while i<=j:
#             m=(i+j)//2
#             print(i,j,m)
#             if tmp[m]<target:
#                 i=m+1
#             elif tmp[m]>target:
#                 j=m-1
#             else:
#                 return True
#         return False

class Solution:
    def searchMatrix(self, matrix, target):
        m=len(matrix)
        if m!=0:
            n=len(matrix[0])
        else:
            n=0
        i=0
        j=m*n-1
        while i<=j:
            mid=(i+j)//2
            l=mid//n
            t=mid%n
            # print(l,t)
            if matrix[l][t]<target:
                i=mid+1
            elif matrix[l][t]>target:
                j=mid-1
            else:
                return True
        return False

def main():
    s=Solution
    matrix=matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34]
]
    target=3
    print(s.searchMatrix(s,matrix,target))

main()