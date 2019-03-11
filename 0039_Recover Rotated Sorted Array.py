# coding=utf-8
'''
描述：给定一个旋转排序数组，在原地恢复其排序
说明：
    什么是旋转数组？
    比如，原始数组为[1,2,3,4], 则其旋转数组可以是[1,2,3,4], [2,3,4,1], [3,4,1,2], [4,1,2,3]
样例：
    样例1:
        [4, 5, 1, 2, 3] -> [1, 2, 3, 4, 5]
    样例2:
        [6,8,9,1,2] -> [1,2,6,8,9]
挑战：使用O(1)的额外空间和O(n)时间复杂度
'''

'''
Python，排序便是...
'''
class Solution:
    """
    @param nums: An integer array
    @return: nothing
    """
    def recoverRotatedSortedArray(self, nums):
        # write your code here
        nums.sort()