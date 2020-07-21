#因为不能重复，所以用坐标就可以
class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        result=[]
        re=[]
        stack=[]
        
        # print(candidates)
        for item in list(set(candidates)):
            if item<=target:
                stack.append((0,item))
        # print(stack)
        while stack:
            tmp=stack.pop()
            tlist=candidates.copy()
        #     # print("tmp",tmp)
        #     #当结果集的层次与当前层次不一致
            while len(re)!=tmp[0]:
                t=re.pop()
        #         s.pop()

            re.append(tmp[1])

            if sum(re)==target:
                result.append(re.copy())

        #     # print("re",re)
        #     #求当前解集的所有候选解

            for i in re:
                tlist.remove(i)
            tlist=list(set(tlist))
            for item in tlist:
                if item <= target-sum(re) and item >= re[-1]:
                    stack.append((tmp[0]+1,item))

        #     # print("stack",stack)
        # print(result)
        return result

def main():
    s=Solution()
    candidates = [10,1,2,7,6,1,5]
    target = 8
    s.combinationSum2(candidates,target)

main()