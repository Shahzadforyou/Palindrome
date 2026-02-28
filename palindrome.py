class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        if(x <0):
            sign = -1
        else:
            sign = +1
        x = abs(x)

        original = x
        reverse = 0
        while x > 0:
            last_digit = x%10
            reverse = reverse *10 + last_digit
            x = x//10
        reverse = reverse*sign
        if(reverse < -2 ** 31 or reverse > 2 ** 31):
            return 0
        else:
            return reverse
        

s = Solution()
print(s.reverse(-1331))