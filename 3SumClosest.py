#time comlexity is O(n^2)
class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        res=0
        mindiffer=1000000
        for i in range(len(nums)):
            left=i+1
            right=len(nums)-1
            while left<right:
                s=nums[i]+nums[left]+nums[right]
                if abs(target-s)<mindiffer:
                    mindiffer=abs(target-s)
                    res=s
                if mindiffer==0:
                    return res
                elif s<target:
                    left+=1
                else:
                    right-=1
        return res

def main():
    s=Solution
    nums=[-1,0,1,2,-1,-4,0,0,0,0]
    print(s.threeSumClosest(s,nums,1))

main()