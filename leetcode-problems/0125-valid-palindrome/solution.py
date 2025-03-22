class Solution(object): 
    def isPalindrome(self, s): 
        def clean_string(s): 
            cleaned_list = [] 
            for char in s: 
                if char.isalnum(): 
                    cleaned_list.append(char.lower()) 
            return ''.join(cleaned_list) 
        
        cleaned_s = clean_string(s) 
        i = len(cleaned_s) 
        
        for n in range(0, i // 2): 
            k = i - n - 1 
            if cleaned_s[n] != cleaned_s[k]: 
                return False 
        return True 
        # s = ''.join(char.lower() for char in s if char.isalnum()) 
        # another logic
