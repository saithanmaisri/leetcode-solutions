class Solution: 
    def isHappy(self, n): 
        sqr = 0 
        while True: 
            while n > 0: 
                rem = n % 10 
                sqr += rem * rem 
                n //= 10 
            if sqr == 1: 
                return True 
            if sqr == 4: 
                return False 
            n = sqr 
            sqr = 0
            
