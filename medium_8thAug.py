# -*- coding: utf-8 -*-
'''
8. String to Integer (atoi)
Implement the myAtoi(string s) function, which converts a 
string to a 32-bit signed integer (similar to C/C++'s atoi function).
'''
#Solution_1
class Solution:
    def myAtoi(self, s: str) -> int:
        num_found = False
        x = ""
        for char in s:
            if char in ["+","-"," "]:
                if num_found:
                    break
                else:
                    x = x + char
            elif char.isnumeric():
                num_found = True
                x = x+ char
            else:
                if num_found:
                    break
                else:
                    return 0
        try:
            x = int(x)
        except:
            return 0
        c = 2**31-1
        if x> c:
            print('ff')
            return 2**31-1
        c = -2**31
        if x<c:
            return -2**31
        return x

'''
Runtime: 32 ms, faster than 81.94% of Python3 online submissions for String to Integer (atoi).
Memory Usage: 14.3 MB, less than 26.29% of Python3 online submissions for String to Integer (atoi).
'''
        

        
        