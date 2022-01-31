class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        to_remove = []
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                to_remove.append(nums[i])
                
        for i in to_remove:
            nums.remove(i)
        return(len(nums))
