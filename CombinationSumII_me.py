#因为不能重复，所以用坐标就可以
class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        result=[]
        re=[]
        stack=[]
        s=[]
        # print(candidates)
        for i in range(len(candidates)):
            if candidates[i]<=target:
                stack.append((0,i))
        while stack:
            tmp=stack.pop()
            # print("tmp",tmp)
            #当结果集的层次与当前层次不一致
            while len(re)!=tmp[0]:
                re.pop()
                s.pop()
            re.append(tmp[1])
            s.append(candidates[tmp[1]])
            # print("re",re)
            #求当前解集的所有候选解
            for i in range(len(candidates)):
                if candidates[i] <= target-sum(s) and i >= re[-1] and i not in re:
                    stack.append((tmp[0]+1,i))
            if sum(s)==target and s not in result:
                result.append(s.copy())
            # print("stack",stack)
        # print(result)
        return result

def main():
    s=Solution()
    candidates = [2,5,2,1,2]
    target = 5
    s.combinationSum2(candidates,target)

main()