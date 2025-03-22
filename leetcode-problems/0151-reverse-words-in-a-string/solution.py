class Solution(object): 
    def reverseWords(self, s): 
        s = s.strip() 
        words = s.split() 
        return " ".join(reversed(words)) 
