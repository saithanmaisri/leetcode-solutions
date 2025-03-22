class Solution(object): 
    def wordPattern(self, pattern, s): 
        """ 
        :type pattern: str 
        :type s: str 
        :rtype: bool 
        """ 
        s = s.split(" ") 
        if len(pattern) != len(s): 
            return False 
        dict_s = {} 
        used_words = set() 
        for i, word in enumerate(s): 
            char = pattern[i] 
            if char not in dict_s: 
                if word in used_words: 
                    return False 
                dict_s[char] = word 
                used_words.add(word) 
            else: 
                if dict_s[char] != word: 
                    return False 
        return True
