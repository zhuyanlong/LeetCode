#其实我很好奇，一列数全排列的顺序是怎么决定的
#算法很巧妙，但不具有一般性，可能只能用来解决这种固定的问题
#这种做法的时间复杂度有点高，要寻求时间复杂度更低的算法
class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)<=1:
            return
        partition=-1
        for i in range(len(nums)-1, 0, -1):
            if nums[i]>nums[i-1]:
                partition=i-1
                break
        if partition==-1:
            nums.revserse()
            return
        for i in range(len(nums)-1,partition,-1):
            if nums[i]>nums[partition]:
                nums[i],nums[partition]=nums[partition],nums[i]
                break
        # print(partition)
        nums[partition+1:len(nums)]=nums[partition+1:len(nums)][::-1]
        # print(nums)
        return

def main():
    nums=[1,4,5,3,2]
    s=Solution
    s.nextPermutation(None,nums)

main()

