class Solution:
    def maxSubArray(self, nums):
        tmpmax=maxsum=nums[0]
        for i in range(1,len(nums)):
            tmpmax=max(tmpmax+nums[i],nums[i])
            if tmpmax>maxsum:
                maxsum=tmpmax
            # print(tmpmax)
        # print(maxsum)
        return maxsum

def main():
    nums=[-2,1,-3,4,-1,2,1,-5,4]
    s=Solution
    s.maxSubArray(None,nums)

main()
