class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        res=[]
        length=len(candidates)
        def DFS(candidates,target,start,res,ret):
            if target==0 and ret not in res:
                res.append(ret)
                return
            for i in range(start,length):
                if target<candidates[i]:
                    return
                DFS(candidates,target-candidates[i],i+1,res,ret+[candidates[i]])
        DFS(candidates,target,0,res,[])
        return res

def main():
    candidates = [2,5,2,1,2]
    target = 5
    s=Solution
    print(s.combinationSum2(None,candidates,target))

main()
