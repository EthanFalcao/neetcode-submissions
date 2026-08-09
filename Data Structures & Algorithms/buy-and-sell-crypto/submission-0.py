class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for n in range(len(prices)):
            print(prices[n])
            for i in range (n,len(prices)):
                profit = prices[i] - prices[n]
                res = max(res,profit)

        return res
        