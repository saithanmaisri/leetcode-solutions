class Solution(object):
    def maxProfit(self, k, prices):
        if k == 0:
            return 0
        if k >= len(prices) // 2:
            profit = 0
            for i in range(1, len(prices)):
                if prices[i] > prices[i - 1]:
                    profit += prices[i] - prices[i - 1]
            return profit

        dp = [[1000, 0] for _ in range(k + 1)]
        for price in prices:
            for i in range(1, k + 1):
                dp[i][0] = min(dp[i][0], price - dp[i - 1][1])
                dp[i][1] = max(dp[i][1], price - dp[i][0])
        return dp[k][1]
