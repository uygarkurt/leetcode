class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = len(sorted(strs, key=lambda x: len(x))[0])
        for idx in range(shortest, -1, -1):
            t_list = []
            for word in strs:
                t_list.append(word[:idx])
            if len(set(t_list)) == 1:
                return strs[0][:idx]
        return ""
