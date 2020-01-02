class Solution:
    def removeDuplicates(self, nums):
        i=0
        for j in range(1,len(nums)):
            if nums[i]!=nums[j]:
                nums[i+1],nums[j]=nums[j],nums[i+1]
                i+=1

def main():
    a=[1,1,2]
    s=Solution
    s.removeDuplicates(None,a)
    print(a)

main()

