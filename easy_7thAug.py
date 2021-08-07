
'''Given a signed 32-bit integer x, return x with its digits reversed. 
   If reversing x causes the value to go outside the signed 32-bit 
   integer range [-231, 231 - 1],
   then return 0.'''
   
# Solution_1
class Solution_1:
    def split(self, string):
        return [char for char in string]
    def reverse(self, x: int) -> int:
        Negative = False
        if x<0:
            Negative = True
            x = x*(-1)
        b = str(x)
        
        c = self.split(b)
        digits = len(c)
        x = 0
        for dig in reversed(c):
            x = x + int(dig)*(10**(digits-1))
            digits = digits - 1
        if Negative:
            x = x*(-1)
        if (-2**31)<x and (2**31 - 1)>x:
            return x
        else:
            return 0
'''
Runtime: 53 ms, faster than 5.77% of Python3 online submissions for Reverse Integer.
Memory Usage: 14.4 MB, less than 12.33% of Python3 online submissions for Reverse Integer.
'''
# Solution_2

class Solution_2:
    def reverse(self, x: int) -> int:
        Negative = False
        if x<0:
            x = x*(-1)
            Negative = True
        a = 0
        while (x/10) !=0:
            b = x%10
            x = int(x/10)
            a = a*10+b
        if Negative:
            print('inside')
            a = a*-1
        if abs(a)<=(2**31 - 1):
            
            return a
        else:
            return 0 

'''
Runtime: 32 ms, faster than 68.90% of Python3 online submissions for Reverse Integer.
Memory Usage: 14.4 MB, less than 12.33% of Python3 online submissions for Reverse Integer.
'''

