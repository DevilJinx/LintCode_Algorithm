# coding=utf-8
'''
描述：设计一个算法，计算出n阶乘中尾部零的个数
样例：
    样例  1:
        输入: 11
        输出: 2    
        样例解释: 
        11! = 39916800, 结尾的0有2个。
    样例 2:
        输入:  5
        输出: 1    
        样例解释: 
        5! = 120， 结尾的0有1个。
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
        sum = 0
        while n != 0:
            n //= 5
            sum += n
        return sum