class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        newl = [0] * len(nums)
        for idx, value in enumerate(nums):
            newl[(idx+k)%len(nums)] = value
            
        nums[:] = newl
