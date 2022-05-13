class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_s = list(set(nums))
        nums_s.sort()
        nums.sort()
        
        
        if nums_s != nums:
            return True
        else:
            return False
