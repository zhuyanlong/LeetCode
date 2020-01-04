#这个递归感觉要精妙很多，除去一个数，然后在剩下的数里递归
def permute(nums):
    if len(nums) == 0: return []
    if len(nums) == 1: return [nums]
    res = []
    for i in range(len(nums)):
        #nums[:i] + nums[i+1:]唯一不包含的就是nums[i]
        for j in permute(nums[:i] + nums[i+1:]):
            # print("j",j)
            # print("nums[i]",nums[i])
            # print("nums[i]+j",[nums[i]]+j)
            res.append([nums[i]] + j)
    return res

def main():
    nums=[1,1,3]
    print(permute(nums))

main()