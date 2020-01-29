class Solution:
    def getPermutation(self, n, k):
        res=""
        num=[1,2,3,4,5,6,7,8,9]
        #k为什么会减一
        #原因如下，比如我在做计算的时候，如果刚好遇到了整除的情况，那么表示我的数字落在了这轮循环的最后一个数上，
        #实际上并没有到下一轮循环，所以k-1可以解决这个问题
        k-=1
        fac=1
        #这个循环用来计算阶乘，阶乘一直成到n-1，因为我只关心所求位后面的排列
        for i in range(1,n):
            fac*=i
        #为什么是倒循环
        #因为要从高位开始确定，所以每次整除都是除以除高位外的其他位
        for i in reversed(range(n)):
            #tmp的值是经过这些循环后落到了哪个数字
            tmp=num[k//fac]
            #添加上这个数字
            res+=str(tmp)
            #从num中移除这个数字
            num.remove(tmp)

            if i!=0:
                #不断缩减k的值
                k%=fac
                fac//=i
        return res

def main():
    n=4
    k=17
    s=Solution
    print(s.getPermutation(None,n,k))

main()