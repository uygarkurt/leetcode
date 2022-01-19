class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        
        previous = self.getRow(rowIndex - 1)
        result = []
        result.append(1)
        for i in range(len(previous)-1):
            tmp = previous[i] + previous[i+1]
            result.append(tmp)
        result.append(1)
        
        return result
