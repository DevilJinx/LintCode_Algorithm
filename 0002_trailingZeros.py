class Solution:
    """
    @param: n: An integer
    @return: An integer, denote the number of trailing zeros in n!
    """
    def trailingZeros(self, n):
        # write your code here, try to do it without arithmetic operators.
        result = 0
        temp = n // 5
        while temp != 0 :
            result += temp
            temp //= 5
        return result