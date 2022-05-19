class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]       
        
        triangle = self.generate(numRows-1)
        last_row = triangle[-1]
        new_row = []
        for i in range(len(last_row)-1):
            new_row.append(last_row[i] + last_row[i+1])
        new_row.insert(0, 1)
        new_row.insert(len(new_row), 1)
        triangle.append(new_row)
        return triangle
