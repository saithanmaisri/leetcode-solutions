class Solution(object): 
    def intToRoman(self, num):  
        dic = [('M', 1000), ('D', 500), ('C', 100), ('L', 50), ('X', 10), ('V', 5), ('I', 1)] 
        res = [] 
        while num > 0: 
            for element in dic: 
                count = 0 
                if num == 4: 
                    res.append('IV') 
                    num -= 4 
                elif num >= 40 and num < 50: 
                    res.append('XL') 
                    num -= 40 
                elif num >= 400 and num < 500: 
                    res.append('CD') 
                    num -= 400 
                elif num == 9: 
                    res.append('IX') 
                    num -= 9 
                elif num >= 90 and num < 100: 
                    res.append('XC') 
                    num -= 90 
                elif num >= 900 and num < 1000: 
                    res.append('CM') 
                    num -= 900 
                while num >= element[1] and count < 3: 
                    num -= element[1] 
                    res.append(element[0]) 
                    count += 1 
                    if count == 3: 
                        break 
            return "".join(res) 
