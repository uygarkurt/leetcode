class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        char_s = []
        char_t = []
        
        for char in s:
            if char not in char_s:
                char_s.append(char)
        for char in t:
            if char not in char_t:
                char_t.append(char)
        
        dic_s = {}
        dic_t = {}
        
        for index, char in enumerate(char_s):
            dic_s[index] = char
        for index, char in enumerate(char_t):
            dic_t[index] = char
            
        inv_s = {v: k for k, v in dic_s.items()}
        inv_t = {v: k for k, v in dic_t.items()}
            
        def encode_word(st, dic):
            new_s = ""
            for char in st:
                new_s += "-" + str(dic[char])
            return new_s
        
        encoded_s = encode_word(s, inv_s)
        encoded_t = encode_word(t, inv_t)
        
        if encoded_s == encoded_t:
            return True
        return False
