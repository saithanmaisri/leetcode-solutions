class Solution: 
    def hashArray(self, s): 
        # 1. Convert to frequency list 
        counter = [0] * 26 
        for char in s: 
            counter[ord(char) - ord('a')] += 1 
        # 2. Convert to hash value using polynomial hash method 
        hash_value = 0 
        for count in counter: 
            hash_value = hash_value * 31 + count # 31 is a commonly used parameter 
        return hash_value 
    
    def groupAnagrams(self, strs): 
        out = [] # solution 
        mp = {} # hash value -> index of out 
        cur_idx = 0 # number of groups 
        for s in strs: 
            hash_val = self.hashArray(s) 
            if hash_val not in mp: 
                mp[hash_val] = cur_idx # found a new group! 
                out.append([s]) 
                cur_idx += 1 
            else: 
                out[mp[hash_val]].append(s) # mp maps hash_num to index of out 
        return out
