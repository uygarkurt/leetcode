class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = defaultdict(int)
        for i in s:
            dic[i] += 1
            
        for key, value in dic.items():
            if value == 1:
                return s.find(key)
            
        return -1
