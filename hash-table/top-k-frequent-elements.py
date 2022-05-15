class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        dic = defaultdict(int)
        for num in nums:
            dic[num] += 1
            
        sorted_dic = {k: v for k, v in sorted(dic.items(), key=lambda item: item[1], reverse=True)}
        return(list(sorted_dic.keys())[:k])
