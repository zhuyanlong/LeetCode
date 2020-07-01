class Solution:
    def singleNumber(self, nums):
        result={}
        for item in nums:
            if item not in result:
                result[item]=1
            else:
                result[item]+=1
        for item in result:
            if result[item]==1:
                return item

def main():
    s=Solution()
    nums=[4,1,2,1,2]
    print(s.singleNumber(nums))

main()