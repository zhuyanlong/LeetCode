#感觉类似在求并集
#最后返回的答案是原始输入集合的不相交集
#暴力解不可行
#重叠区间的判断
class Solution:
    def merge(self, intervals):
        res=[]
        intervals.sort(key= lambda x:x[0])
        for i in range(len(intervals)):
            if res==[]:
                res.append(intervals[i])
            else:
                size=len(res)
                if intervals[i][0]<=res[size-1][1]:
                    res[size-1][1]=max(intervals[i][1],res[size-1][1])
                else:
                    res.append(intervals[i])
        print(res)
        return res

def main():
    intervals=[[1,4],[4,5]]
    s=Solution
    s.merge(None,intervals)

main()
