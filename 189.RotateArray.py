class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)==0:
            return
        if k>len(nums):
            k=k%len(nums)
        # for i in range(k):
        #     tmp=nums[-1]
        #     for j in range(len(nums)-2,-2,-1):
        #         nums[j+1]=nums[j]
        #     nums[0]=tmp
        # print(nums)

        # print(k)
        a=nums[-k:]
        b=nums[:len(nums)-k]
        tmp=a+b
        for i in range(len(nums)):
            nums[i]=tmp[i]
        print(nums)

# class Solution:
#     def rotate(self, nums, k):
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         if len(nums)==0:
#             return
#         if k>len(nums):
#             k=k%len(nums)


def main():
    nums = [1,2,3,4,5,6,7]
    k = 4
    s=Solution()
    s.rotate(nums,k)

main()