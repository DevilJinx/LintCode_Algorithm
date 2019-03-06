# coding=utf-8
'''
描述：给定一个列表，该列表中的每个元素要么是个列表，要么是整数。将其变成一个只包含整数的简单列表
样例：
    样例  1:
        输入: [[1,1],2,[1,1]]
        输出:[1,1,2,1,1]    
        样例解释:
        将其变成一个只包含整数的简单列表。
    样例 2:
        输入: [1,2,[1,2]]
        输出:[1,2,1,2]    
        样例解释: 
        将其变成一个只包含整数的简单列表。   
    样例 3:
        输入:[4,[3,[2,[1]]]]
        输出:[4,3,2,1]    
        样例解释: 
        将其变成一个只包含整数的简单列表。
挑战：请用非递归方法尝试解答这道题
'''

class Solution(object):

    # @param nestedList a list, each element in the list 
    # can be a list or integer, for example [1,2,[1,2]]
    # @return {int[]} a list of integer
    def flatten(self, nestedList):
        # Write your code here
        stack = [nestedList]
        flatten_list = []
        
        while stack:
            top = stack.pop()
            if isinstance(top, list):
                for elem in reversed(top):
                    stack.append(elem)
            else:
                flatten_list.append(top)
        return flatten_list