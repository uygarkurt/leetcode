class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        right = 1
        left = 0
        nums = sorted(nums)
        
        total = 0
        while right < len(nums):
            total += min(nums[right], nums[left])
            right += 2
            left += 2
            
        return total
