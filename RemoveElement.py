#尝试双头指针
#双尾指针
#头尾指针
#只有双尾指针可以成功
class Solution:
    def removeElement(self, nums, val):
        j=len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if nums[i]==val:
                nums[i],nums[j]=nums[j],nums[i]
                j-=1
        return j+1

def main():
    a=[0,1,2,2,3,0,4,2]
    s=Solution
    print(s.removeElement(None,a,2))
    print(a)

main()