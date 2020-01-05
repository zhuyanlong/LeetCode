class Solution:
    def rotate(self, matrix):
        for i in range(len(matrix)):
            for j in range(i,len(matrix[i])):
                # print("i,j",i,j)
                # print(matrix)
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for i in range(len(matrix)):
            for j in range(int(len(matrix)/2)):
                matrix[i][j],matrix[i][len(matrix)-1-j]=matrix[i][len(matrix)-1-j],matrix[i][j]
        print(matrix)


def main():
    matrix=[
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
    s=Solution
    s.rotate(None, matrix)

main()


