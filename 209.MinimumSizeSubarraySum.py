#时间复杂度O(n)
class Solution:
    def minSubArrayLen(self, s, nums):
        res=float('inf')
        left=0
        right=1
        if s==0:
            return 0
        if len(nums)==0:
            return 0
        tmp=nums[0]
        while left<right:
            if tmp>=s:
                if res>=right-left:
                    res=right-left
                tmp-=nums[left]
                left+=1 
            else:
                if right<len(nums):
                    right+=1
                    tmp+=nums[right-1]
                else:
                    #这个break要好好理解下，原因是这样的，假如我现在right到了头都没能满足tmp>=s，
                    #那么你去执行另一个代码段也一定不可能满足的
                    break
            # print(left,right,tmp)
        if res==float('inf'):
            return 0
        return res

def main():
    nums = [2,3,1,2,4,3]
    # nums=[]
    s = 7
    sol=Solution()
    print(sol.minSubArrayLen(s,nums))

main()
