'''
type:
nums: list
target: int
求出nums中所有和为target的数对
'''
def twoSum(nums, target):
    nums.sort()
    result=[]
    for i in range(len(nums)):
        j=len(nums)-1
        while i<j:
            if nums[i]+nums[j]==target:
                result.append([nums[i],nums[j]])
                break
            else:
                j-=1
    return result

def main():
    nums=[-2,-1,0,1,2,3]
    target=0
    print(twoSum(nums,target))
main()