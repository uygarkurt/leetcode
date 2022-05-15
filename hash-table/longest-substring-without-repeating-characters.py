class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        elif len(list(set(s))) == 1:
            return 1
        
        dic = {}
        l = []
        char = 0
        counter = 0
        while char < len(s):
            if s[char] not in l:
                l.append(s[char])
                char += 1
            else:
                dic["".join(l)] = len(l)
                l = []
                counter += 1
                char = counter
         
        if len(dic) > 0:
            max_in_dic = sorted(list(dic.values()), reverse=True)[0]
        else:
            max_in_dic = -1
            
        if len(l) > max_in_dic:
            return(len(l))
        return(max_in_dic)
