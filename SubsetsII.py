class Solution:
    def subsetsWithDup(self, nums):
        res=[]
        if len(nums)==0:
            return []
        nums.sort()
        stack=[[]]
        while stack:
            top=stack.pop()
            for i in range(len(nums)):
                if i not in top:
                    if len(top)==0 or i >top[-1]:
                        tmp=top.copy()
                        tmp.append(i)
                        if tmp not in stack:
                            stack.append(tmp)
            tmp=[]
            for i in top:
                tmp.append(nums[i])
            if tmp not in res:
                res.append(tmp)
        return res

def main():
    s=Solution
    nums=[4,4,4,1,4]
    print(s.subsetsWithDup(s,nums))

main()