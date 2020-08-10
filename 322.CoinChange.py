class Solution:
    def coinChange(self, coins, amount):
        n=amount+1
        dp=[amount+1 for i in range(n)]
        dp[0]=0
        #i是dp第找i分钱所需要的硬币数
        #dp数组是找i分钱所需要的最小硬币数
        for i in range(1,n):
            for j in range(len(coins)):
                if i-coins[j]>=0:
                    dp[i]=min(dp[i],dp[i-coins[j]]+1)
                # print("Y")
        # print(dp)
        if dp[amount]==amount+1:
            return -1
        return dp[amount]


def main():
    coins = [1]
    amount=3
    s=Solution()
    print(s.coinChange(coins,amount))

main()


