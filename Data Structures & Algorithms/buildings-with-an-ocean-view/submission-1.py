class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res = [len(heights) - 1] # this gives me the last index 
        print(len(heights) - 1)
        print(res)
        for n in range( len(heights)-2, -1,-1):
            if heights[n] > heights[res[-1]]:
                res.append(n)

        res.reverse()

        return res 
        