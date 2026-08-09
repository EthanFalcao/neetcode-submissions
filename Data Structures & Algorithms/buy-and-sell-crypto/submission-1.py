class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_p = prices[0]
        res = 0

        for n in prices:
            res = max(n - min_p, res)
            min_p = min(n, min_p)
            
        
        return res

        