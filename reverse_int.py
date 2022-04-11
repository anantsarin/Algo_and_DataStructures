
# Given a 32-bit signed integer, reverse digits of an integer.

# Note:
# Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321
# Example 3:

# Input: x = 120
# Output: 21
# Example 4:

# Input: x = 0
# Output: 0

# Constraints:
# -2^31 <= x <= 2^31 - 1

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if (x >= 2147483647 or x <= -2147483648):
            return 0
        if x==0:
            return x
        negative_flag = 1
        if x < 0:
            x = -1*x
            negative_flag = -1
        rev = 0
        while (x != 0):
            rev = (x%10) + rev*10
            x= x/10
            if (rev >= 2147483647 or rev <= -2147483648):
                return 0
        return (rev*negative_flag)
