class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        counter_list = []
        for i in nums:
            if i == 1:
                counter += 1
            else:
                counter_list.append(counter)
                counter = 0
        counter_list.append(counter) 
        return max(counter_list)
