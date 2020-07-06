class Solution:
    def majorityElement(self, nums):
        result={}
        nums.sort()
        for item in nums:
            if item not in result:
                result[item]=1
            else:
                result[item]+=1
            if result[item]>len(nums)//2:
                return item
        return 0

def main():
    nums=[2,2,1,1,1,2,2]
    s=Solution()
    print(s.majorityElement(nums))

main()