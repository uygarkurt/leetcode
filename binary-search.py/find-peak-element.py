class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        for counter in range(len(nums)):
            if counter == 0:
                if nums[counter] > nums[counter+1]:
                    return counter
            elif counter == len(nums)-1:
                if nums[counter] > nums[counter-1]:
                    return counter
            else:
                if nums[counter] > nums[counter+1] and nums[counter] > nums[counter-1]:
                    return counter
