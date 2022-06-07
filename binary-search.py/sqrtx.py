class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        for i in range(x+1):
            if i * i <= x and (i+1) * (i+1) > x:
                return i
