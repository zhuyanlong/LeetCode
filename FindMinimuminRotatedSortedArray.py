class Solution:
    def findMin(self, nums):
        left=0
        right=len(nums)-1
        while left<right:
            mid=(left+right)//2
            if nums[mid]>nums[right]:
                left=mid+1
            else:
                right=mid
            print(left,mid,right)
        return nums[left]

def main():
    s=Solution()
    nums=[4,5,6,7,0,1,2]
    print(s.findMin(nums))

main()