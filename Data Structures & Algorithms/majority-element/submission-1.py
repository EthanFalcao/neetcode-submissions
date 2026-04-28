class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major = defaultdict(int)

        for n in nums:
            major[n] += 1 

        max_val = max(major.values())

        for n in major.keys():
            if major[n] == max_val:
                return n 




        