#区间交集
class Solution:
    def intervalIntersection(self, A, B):
        result=[]
        for ia in A:
            for ib in B:
                if ib[0]>ia[1]:
                    break
                if ia[0]>ib[1]:
                    continue
                if ia[0]<ib[0] and ia[1]>ib[1]:
                    result.append(ib)
                elif ia[0]>ib[0] and ia[1]<ib[1]:
                    result.append(ia)
                else:
                    result.append([max(ia[0],ib[0]),min(ia[1],ib[1])])
        # print(result)
        return result


def main():
    A=[[0,2],[5,10],[13,23],[24,25]]
    B=[[1,5],[8,12],[15,24],[25,26]]
    s=Solution()
    s.intervalIntersection(A,B)

main()