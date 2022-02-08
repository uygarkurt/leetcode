class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        import numpy as np
        expected = np.array(sorted(heights))
        
        answer = (expected != np.array(heights)).sum()
        return answer
