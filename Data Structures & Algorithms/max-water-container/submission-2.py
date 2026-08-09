class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights)-1
        res =0
        while l<r:
            prod = min(heights[l],heights[r]) * abs(l-r)
            res = max(res,prod)

            if heights[l] <heights[r]:
                l+=1
            else:
                r -=1
        return res 
