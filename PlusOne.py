#时间复杂度O(n)
# class Solution:
#     def plusOne(self, digits):
#         n=len(digits)-1
#         sum=0
#         res=[]
#         for i in range(n,-1,-1):
#             sum+=pow(10,n-i)*digits[i]
#         sum+=1
#         while sum!=0:
#             tmp=sum%10
#             sum//=10
#             res.insert(0,tmp)
        # print(res)

#更快的方式，不需要将list转换成数字，直接用flag位进位
#实际上这样子写，实际复杂度反而更高了，合并算法执行路径，大概是降低复杂度最好的办法了
# class Solution:
#     def plusOne(self, digits):
#         carry=0
#         n=len(digits)-1
#         if digits[n]+1!=10:
#             digits[n]+=1
#             return digits
#         else:
#             carry=1
#             for i in range(n,-1,-1):
#                 if digits[i]+carry!=10:
#                     digits[i]+=1
#                     return digits
#                 else:
#                     carry=1
#                     digits[i]=0
#         digits[0]=0
#         digits.insert(0,1)
#         return digits

#最优快速解法
class Solution:
    def plusOne(self, digits):
        carry=1
        n=len(digits)-1
        for i in range(n,-1,-1):
            if digits[i]+carry==10:
                digits[i]=0
                carry=1
            else:
                digits[i]+=1
                carry=0
                return digits
        if carry==1:
            digits.insert(0,1)
        return digits

def main():
    s=Solution
    tmp=[9,9,9]
    print(s.plusOne(None,tmp))

main()