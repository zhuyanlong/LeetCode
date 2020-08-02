# class Solution:
#     def maxProfit(self, prices):
#         result=[0 for i in range(len(prices))]
#         for i in range(1,len(prices)):
#             result[i]=prices[i]-min(prices[0:i])
#         # print(result)
#         return max(result)

#DP法
class Solution:
    def maxProfit(self, prices):
        maxpro=0
        for i in range(1,len(prices)):
            if prices[i]-prices[i-1]>maxpro:
                maxpro=prices[i]-prices[i-1]
            if prices[i]>prices[i-1]:
                prices[i]=prices[i-1]
        return maxpro


def main():
    s=Solution()
    prices=[7,1,5,3,6,4]
    print(s.maxProfit(prices))

main()