'''
描述： 
    设计一个算法，计算出n阶乘中尾部零的个数
样例：
    11！=39916800，因此应该返回2
挑战：
    O(logN)的时间复杂度
'''

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