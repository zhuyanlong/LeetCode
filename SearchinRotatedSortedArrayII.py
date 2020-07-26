#这种题目必须和中间元素作比较
class Solution:
    def search(self, nums, target):
        #数据去重，目前想不到更好的办法
        nums=list(set(nums))
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)//2
            # print(left,mid,right)
            if target==nums[mid]:
                return True
            if nums[mid] < nums[right]:
                if target>nums[mid]:
                    if target>nums[right]:
                        right=mid-1
                    else:
                        if target==nums[right]:
                            return True
                        left=mid+1
                else:
                    right=mid-1
            else:
                if target>nums[mid]:
                    left=mid+1
                else:
                    if target>nums[right]:
                        right=mid-1
                    else:
                        if target==nums[right]:
                            return True
                        left=mid+1

def main():
    s=Solution()
    nums=[3,1,1]
    target=1
    print(s.search(nums,target))

main()