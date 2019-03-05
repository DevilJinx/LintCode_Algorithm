# coding=utf-8
'''
描述：给出两个整数a和b, 求他们的和
说明：
    a和b都是 32位 整数么？
        是的
    我可以使用位运算符么？
        当然可以
样例：
    样例  1:
        输入:  a = 1, b = 2
        输出: 3    
        样例解释: 
        返回a+b的结果.
    样例 2:
        输入:  a = -1, b = 1
        输出: 0   
        样例解释: 
        返回a+b的结果.
挑战：
    显然你可以直接 return a + b，但是你是否可以挑战一下不这样做？（不使用++等算数运算符）
'''

class Solution:
    """
    @param: : An integer
    @param: : An integer
    @return: The sum of a and b
    """

    def aplusb(self, a, b):
        INT_RANGE = 0xFFFFFFFF
        while b != 0:
            a, b = a ^ b, (a & b) << 1
            a &= INT_RANGE
        return a if a >> 31 <= 0 else a ^ ~INT_RANGE