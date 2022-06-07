class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l = []
        for digit in nums1:
            if digit in nums2:
                l.append(digit)
                nums2.remove(digit)
                
        return(l)
