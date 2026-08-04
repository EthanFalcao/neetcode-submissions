class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res = [len(heights) - 1] # this gives me the last index 
        for n in range( len(heights)-2, -1,-1): # range(starting point, last point, the direction or step)
            if heights[n] > heights[res[-1]]:
                res.append(n)

        res.reverse()
        return res 
        