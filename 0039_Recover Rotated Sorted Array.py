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

class Solution:
    """
    @param nums: An integer array
    @return: nothing
    """
    def recoverRotatedSortedArray(self, nums):
        # write your code here
        n = len(nums)
        for i in range(n):
            if nums[0] >= nums[-1]:
                temp = nums[0]
                nums.remove(nums[0])
                nums.append(temp)
            else:
                return

'''
1、不建立新数组，在原数组上操作
2、只循环依次数组
依次获取数组第一个和最后一个元素比较，若[0]>[-1]，则移除[0]并追加到数组末尾直到[0]<[-1]
'''