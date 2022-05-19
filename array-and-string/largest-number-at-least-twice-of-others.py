class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        sorted_nums = sorted(nums, reverse=True)
        if sorted_nums[0] >= 2*sorted_nums[1]:
            return nums.index(sorted_nums[0])
        else: return -1
