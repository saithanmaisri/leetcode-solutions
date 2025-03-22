class Solution(object): 
    def lengthOfLastWord(self, s): 
        wordlist = s.split() 
        if wordlist: 
            return len(wordlist[-1]) 
        return 0
