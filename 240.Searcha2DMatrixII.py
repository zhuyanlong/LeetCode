class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix)==0:
            return False
        if len(matrix[0])==0:
            return False
        i=0
        #这块只需要判断大于，到每一行判断的时候，再去判断小于
        for i in range(len(matrix)):
            if target<=matrix[i][-1] and target>=matrix[i][0]:
                j=0
                while j!=len(matrix[i]) and matrix[i][j]<=target:
                    print(matrix[i][j])
                    if matrix[i][j]==target:
                        return True
                    j+=1
        return False
        #也可以用python内置的in来判断，时间空间复杂度更低

def main():
#     matrix=[
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
    matrix=[[1],[6]]
    target=6
    s=Solution()
    print(s.searchMatrix(matrix,target))

main()
