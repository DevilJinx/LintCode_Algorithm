'''
描述：
    给出两个整数a和b, 求他们的和。
说明：
    a和b都是32位整数么？
        是的
    我可以使用位运算符么？
        当然可以
样例：
    如果a=1并且b=2，返回3
挑战：
    显然你可以直接return a + b，但是你是否可以挑战一下不这么做？（不使用+等算术运算符）
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