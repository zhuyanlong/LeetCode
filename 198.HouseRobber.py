class Solution:
    def rob(self, nums):
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums[0],nums[1])
        for i in range(2,len(nums)):
            nums[i]=nums[i]+max(nums[:i-1])
        return max(nums[-1],nums[-2])

def main():
    s=Solution()
    nums=[2,7,9,3,1]
    print(s.rob(nums))

main()