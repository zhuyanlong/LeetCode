#这个代码写的其实不是特别好，因为里面有几种特殊情况，都进行分别处理了，最好的代码还是可以统一处理某类情况

class Solution:
    def searchRange(self, nums, target):
        if len(nums)==0:
            return [-1,-1]
        if len(nums)==1 and nums[0]==target:
            return [0,0]
        res=[]
        left=self.searchLeftRange(self,nums,target)
        # print(res)
        right=self.searchRightRange(self,nums,target)
        if left==right:
            res=[-1,-1]
        else:
            res.append(left)
            res.append(right-1)
        print(res)
        return res

    #这个函数的用处是逼近左侧区间
    def searchLeftRange(self,nums,target):
        left=0
        right=len(nums)-1
        while left<right:
            mid=(left+right)//2
            if nums[mid]<target:
                left=mid+1
            else:
                right=mid
        return left

    def searchRightRange(self,nums,target):
        left=0
        right=len(nums)-1
        while left<right:
            mid=(left+right)//2
            if nums[mid]<=target:
                left=mid+1
            else:
                right=mid
            if nums[right]==target:
                return right+1
        return left

def main():
    nums=[5,7,7,8,8,8]
    target=1
    s=Solution
    s.searchRange(s,nums,target)

main()