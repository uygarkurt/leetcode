class Solution:
    def isHappy(self, n: int) -> bool:
        numbers = []
        while True:
            str_n = str(n)
            sm = 0
            for digit in str_n:
                sm += int(digit)**2
            n = sm
            if n == 1:
                return True
            elif n in numbers:
                return False
            numbers.append(n)
