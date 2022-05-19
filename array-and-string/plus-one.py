class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [str(digit) for digit in digits]
        number = int("".join(digits))
        number += 1
        new_l = [int(i) for i in str(number)]
        return new_l
