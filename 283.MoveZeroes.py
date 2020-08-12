class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        count=0
        i=0
        while i!=len(nums):
            if nums[i]==0:
                del nums[i]
                i-=1
                count+=1
            i+=1
        while count!=0:
            nums.append(0)
            count-=1
        # print(nums)

def main():
    nums=[0,1,0,3,12]
    s=Solution()
    s.moveZeroes(nums)

main()