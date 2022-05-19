class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        from collections import defaultdict
        dic = defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                dic[i+j].append(mat[i][j])
                
        answer = []
        for i in range(len(dic)):
            if i%2 == 0:
                answer.append(list(dic.values())[i][::-1])
            else:
                answer.append(list(dic.values())[i])
                
        return [i for j in answer for i in j]
