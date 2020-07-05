#列表法
# class Solution:
#     def twoSum(self, numbers, target):
#         result=[]
#         for i in range(len(numbers)):
#             tmp=target-numbers[i]
#             for j in range(i+1,len(numbers)):
#                 if tmp==numbers[j]:
#                     result.append(i+1)
#                     result.append(j+1)
#                     return result
#                 elif tmp<numbers[j]:
#                     break
#             if numbers[i]>target//2:
#                 break
#         return result

#字典法
class Solution:
    def twoSum(self, numbers, target):
        b=[i for i in range(1, len(numbers)+1)]
        numdict=dict(zip(numbers,b))
        result=[]
        for i in range(len(numbers)):
            tmp=target-numbers[i]
            if tmp in numdict:
                result.append(i+1)
                result.append(numdict[tmp])
                return result
        return result

def main():
    s=Solution()
    numbers=[2,7,11,15]
    target = 9
    print(s.twoSum(numbers,target))

main()