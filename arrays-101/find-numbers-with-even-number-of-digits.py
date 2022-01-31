class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        str_nums = []
        for i in nums:
            str_nums.append(str(i))
            
        counter = 0
        for i in str_nums:
            if len(i)%2 == 0:
                counter += 1
                
        return counter
