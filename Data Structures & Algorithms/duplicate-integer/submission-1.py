class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res = Counter(nums)

        for n in res.values():
            if n >1:
                return True 
        return False 

   