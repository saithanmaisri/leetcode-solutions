class Solution(object): 
    def isSubsequence(self, s, t): 
        first = 0 
        second = 0 
        length1 = len(s) 
        length2 = len(t) 
        while first < length1 and second < length2: 
            if s[first] == t[second]: 
                first += 1 
            second += 1 
        return first == length1
