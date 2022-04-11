class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if (x >= 2147483647 or x <= -2147483648):
            return False
        if x < 0 :
            return False
        y = x
        rev = 0
        while y > 0:
            rev = rev*10 + y%10
            y = y/10
            if rev >= 2147483647:
                return False
        if rev == x:
            return True
        return False
