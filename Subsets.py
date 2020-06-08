class Solution:
    def subsets(self, nums):
        res=[]
        if len(nums)==0:
            return []
        stack=[[]]
        res.append([])
        while stack:
            top=stack.pop()
            for item in nums:
                if len(top)==0 or item >top[-1]:
                    tmp=top.copy()
                    tmp.append(item)
                    stack.append(tmp)
            res.append(tmp)
        return res

def main():
    s=Solution
    nums=[1,2,5,3,4]
    print(s.subsets(s,nums))

main()