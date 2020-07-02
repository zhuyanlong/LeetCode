#这种做法思想比较简单，正数就看前一个值，负数无限向前回溯，但是问题就是时间和空间复杂度会很高，所以要想一种更好的做法
# class Solution:
#     def maxProduct(self, nums):
#         if len(nums)==0:
#             return 0
#         result=[0 for i in range(len(nums))]
#         result[0]=nums[0]
#         for i in range(1,len(nums)):
#             result[i]=max(nums[i],nums[i]*result[i-1])
#             if nums[i]<0:
#                 tmp=nums[i]
#                 for j in range(i-1,-1,-1):
#                     tmp*=nums[j]
#                     if tmp>result[i]:
#                         result[i]=tmp
#         # print(result)
#         return max(result)

#每次遍历有两个候选值，一个是之前所有中的最大值，还有一个是所有中的最小值
#现在来解释这个问题，最大值不用说，下一个最大值是可能从前一个最大值中产生的，我之前的写法就遵守这点
#需要解释的是另一个问题，就是最小值，因为有可能是负数，假如我当前遍历的是个负数，那么我之前的最小值和现在的负数相乘是有可能产生最大值的
#这点是这道题的基本思想
# class Solution:
#     def maxProduct(self, nums):
#         if len(nums)==0:
#             return 0
#         maxnum=nums[0]
#         minnum=nums[0]
#         result=nums[0]
#         for i in range(1,len(nums)):
#             a=nums[i]*maxnum
#             b=nums[i]*minnum
#             c=nums[i]
#             maxnum=max([a,b,c])
#             minnum=min([a,b,c])
#             if maxnum>result:
#                 result=maxnum
#         return result

class Solution:
    def maxProduct(self, nums):
        if len(nums)==0:
            return 0
        result=[[0,0] for i in range(len(nums))]
        result[0]=[nums[0],nums[0]]
        for i in range(1,len(nums)):
            result[i][0]=max(nums[i],nums[i]*result[i-1][0],nums[i]*result[i-1][1])
            result[i][1]=min(nums[i],nums[i]*result[i-1][0],nums[i]*result[i-1][1])
        print(result)
        # return max(result)

def main():
    s=Solution()
    nums=[-1,-2,-9,-6]
    print(s.maxProduct(nums))

main()