class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        from collections import defaultdict
        dic = defaultdict(int)
        
        for num in nums:
            dic[num] += 1
            
        for key, value in dic.items():
            if value >= 2:
                return key
