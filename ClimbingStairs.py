#实际上是一个斐波那契数列
class Solution:
    def climbStairs(self, n):
        dp=[1 for i in range(n+1)]
        for i in range(2,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]
def main():
    n=4
    s=Solution
    print(s.climbStairs(None,n))
main()