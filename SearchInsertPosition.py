class Solution:
    def searchInsert(self, nums, target):
        i=0
        j=len(nums)-1
        if target<=nums[0]:
            return 0
        if target>nums[j]:
            return j+1
        while i!=j-1:
            m=int((i+j+1)/2)
            if nums[m]<target:
                i=m
            elif nums[m]>target:
                j=m
            else:
                return m
        return i+1

def main():
    nums=[1,3,5,6]
    target=5
    s=Solution
    print(s.searchInsert(None,nums,target))

main()