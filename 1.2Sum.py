'''
type:
nums: list
target: int
求出nums中所有和为target的数对
'''
# def twoSum(nums, target):
#     nums.sort()
#     result=[]
#     for i in range(len(nums)):
#         j=len(nums)-1
#         while i<j:
#             if nums[i]+nums[j]==target:
#                 result.append([nums[i],nums[j]])
#                 break
#             else:
#                 j-=1
#     return result

class Solution:
    def twoSum(self, nums, target):
        dic={}
        for i in range(len(nums)):
            dic[nums[i]]=i
        # print(dic)
        for i in range(len(nums)):
            tmp=target-nums[i]
            if tmp in dic and i!=dic[tmp]:
                return [i,dic[tmp]]
        return []

def main():
    nums=[-2,-1,0,1,2,3]
    target=0
    print(twoSum(nums,target))
main()
