class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for n in range(len(nums) - 2):
            if n > 0 and nums[n] == nums[n - 1]:
                continue  # skip duplicate anchors

            l, r = n + 1, len(nums) - 1
            while l < r:
                tmp_sum = nums[l] + nums[n] + nums[r]

                if tmp_sum == 0:
                    res.append([nums[n], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1  # skip duplicate left values
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1  # skip duplicate right values
                elif tmp_sum > 0:
                    r -= 1
                else:
                    l += 1

        return res