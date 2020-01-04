#DFS的题目还需多做
class Solution:
    def combinationSum(self, candidates, target):
        candidates.sort()
        res=[]
        length=len(candidates)
        def DFS(candidates,target,start,res,ret):
            if target==0:
                res.append(ret)
                return
            for i in range(start,length):
                if target<candidates[i]:
                    return
                DFS(candidates,target-candidates[i],i,res,ret+[candidates[i]])
        DFS(candidates,target,0,res,[])
        return res

def main():
    candidates = [8,7,4,3]
    target = 11
    s=Solution
    print(s.combinationSum(None,candidates,target))

main()
