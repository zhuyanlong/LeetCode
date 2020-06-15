class Solution:
    def getRow(self, rowIndex):
        res=[0 for i in range(rowIndex+1)]
        res[0]=1
        for i in range(1,rowIndex+1):
            for j in range(i,0,-1):
                print(res)
                print(j)
                res[j]+=res[j-1]
        return res
def main():
    s=Solution
    print(s.getRow(s,6))

main()

