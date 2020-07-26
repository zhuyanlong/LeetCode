#基本上把时间复杂度保持在O(nlgn)就可以了，空间复杂度要低一些
class Solution:
    def findKthLargest(self, nums, k):
        nums.sort()
        return nums[-k]

def main():
    s=Solution()
    nums=[3,2,3,1,2,4,5,5,6]
    k=4
    print(s.findKthLargest(nums,k))

main()