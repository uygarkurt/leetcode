class Solution:
    def reverseString(self, s: List[str]) -> None:
        
        def solver(left, right):
            if left < right:
                tmp = s[left]
                s[left] = s[right]
                s[right] = tmp
                solver(left+1, right-1)
                
        solver(0, len(s)-1)
