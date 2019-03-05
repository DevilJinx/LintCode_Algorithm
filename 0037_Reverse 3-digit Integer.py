# coding=utf-8
'''
描述：反转一个只有3位数的整数。
样例：
    样例 1:
        输入: number = 123
        输出: 321
    样例 2:
        输入: number = 900
        输出: 9
'''

class Solution:
    """
    @param number: A 3-digit number.
    @return: Reversed number.
    """
    def reverseInteger(self, number):
        # write your code here
        unit = int(number % 10)
        ten = int(number % 100 / 10)
        hun = int(number / 100)
        return (unit * 100 + ten * 10 + hun)
