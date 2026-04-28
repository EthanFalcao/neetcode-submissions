class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_nums = {}

        for n in nums: 
            if n in count_nums:
                count_nums[n] +=1
            else: 
                count_nums[n] =1

        sorted_keys = sorted(count_nums, key=count_nums.get)
        print(sorted_keys)
        
        return sorted_keys[-k:]
 
        