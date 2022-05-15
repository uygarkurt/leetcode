class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        intersect = []
        for index, res in enumerate(list1):
            if res in list2:
                intersect.append((res, index+list2.index(res)))
                
        sorted_intersect = sorted(intersect, key=lambda x: x[1])
        least_index = sorted_intersect[0][1]
        
        answer = []
        for tup in sorted_intersect:
            if tup[1] == least_index:
                answer.append(tup[0])
            
        return answer
