class Solution:
    def subsets(self, nums):
        res=[]
        if len(nums)==0:
            return []
        stack=[[]]
        while stack:
            top=stack.pop()
            if top not in res:
                res.append(top.copy())
            for item in nums:
                if item not in top:
                    if len(top)==0 or item >top[-1]:
                        tmp=top.copy()
                        tmp.append(item)
                        res.append(tmp)
                        stack.append(tmp)
        return res

def main():
    s=Solution
    nums=[1,3,2,4]
    print(s.subsets(s,nums))

main()