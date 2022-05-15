class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        for index, num in enumerate(nums):
            if num in dic and abs(index - dic[num]) <= k:
                return True
            dic[num] = index
            
        return False
