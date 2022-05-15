class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        dic = defaultdict(list)
        
        for st in strs:
            dic["".join(sorted(list(st)))].append(st)
            
        return(list(dic.values()))
