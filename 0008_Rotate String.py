# coding=utf-8
'''
描述：给定一个字符串（以字符数组的形式给出）和一个偏移量，根据偏移量原地旋转字符串(从左向右旋转)
样例：
    样例  1:
        输入:  str="abcdefg", offset = 3
        输出: "efgabcd"  
        样例解释: 
        返回旋转后的字符串。
    样例 2:
        输入: str="abcdefg", offset = 0
        输出: "abcdefg"    
        样例解释: 
        返回旋转后的字符串
    样例 3:
        输入: str="abcdefg", offset = 1
        输出: "gabcdef"    
        样例解释: 
        返回旋转后的字符串
    样例 4:
        输入: str="abcdefg", offset =2
        输出:"fgabcde"    
        样例解释: 
        返回旋转后的字符串
挑战：在数组上原地旋转，使用O(1)的额外空间
'''

class Solution:
    """
    @param str: An array of char
    @param offset: An integer
    @return: nothing
    """
    def rotateString(self, str, offset):
        # write your code here
        if not offset:
            return
        if not str:
            return
        
        n = len(str)
        offset = offset % n
        for i in range(offset):
            t = str.pop()
            str.insert(0, t)