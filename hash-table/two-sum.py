class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        
        for idx, value in enumerate(nums):
            diff = target - value
            if diff in d:
                return [d[diff], idx]
            d[value] = idx
