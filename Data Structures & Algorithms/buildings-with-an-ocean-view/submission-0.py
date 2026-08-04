class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res = []

        for n in range(0,len(heights)):
            skip = True
            for z in range(n+1, len(heights)):
                if heights[n] > heights[z]:
                    continue 
                else:
                    skip = False
                    break
                    
            if skip == True:
                res.append(n)
        return sorted(res)            
