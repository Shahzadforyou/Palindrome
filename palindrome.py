class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        self.original = x
        self.reverse = 0
        while x > 0:
            self.last_digit = x%10
            self.reverse = self.reverse *10 + self.last_digit
            x = x//10
        if(self.reverse == self.original):
            return True
        else:
            return False
        

s = Solution()
print(s.reverse(1334))