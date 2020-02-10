class Solution:
    def generate(self, numRows):
        if numRows==0:
            return []
        elif numRows==1:
            return [[1]]
        elif numRows==2:
            return [[1],[1,1]]
        else:
            res=[[1],[1,1]]
            for i in range(2,numRows):
                tmp=[1,1]
                for j in range(1,i):
                    num=res[i-1][j-1]+res[i-1][j]
                    # print("num",num)
                    tmp.insert(j,num)
                res.append(tmp)
            return res

def main():
    numRows=4
    s=Solution
    print(s.generate(None,numRows))

main()