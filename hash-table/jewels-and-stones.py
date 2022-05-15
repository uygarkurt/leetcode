class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        from collections import defaultdict
        dic = defaultdict(int)
        for stone in stones:
            if stone in jewels:
                dic[stone] += 1
                
        x = sum(list(dic.values()))
        return x
