class Solution:
    def numTrees(n):
        num=[]
        num.append(1)
        num.append(1)
        num.append(2)
        if n <=2:
            return num[n]
        for i in range(3,n+1):
            sum=0
            for j in range(1,i+1):
                #左侧*右侧
                sum+=num[j-1]*num[i-j]
            num.append(sum)
        return num[n]

def main():
    s=Solution
    print(s.numTrees(4))

main()