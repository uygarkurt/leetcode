class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even_list = []
        odd_list = []
        for i in nums:
            if i % 2 == 0:
                even_list.append(i)
            else:
                odd_list.append(i)

        new_list = even_list + odd_list
        return new_list
