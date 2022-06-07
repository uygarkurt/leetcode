# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        first = 1
        last = n
        while True:
            middle = (first + last) // 2
            if isBadVersion(middle) == False:
                first = middle + 1
            elif isBadVersion(middle) == True:
                if isBadVersion(middle-1) == False:
                    return middle
                last = middle - 1
