# coding=utf-8
'''
描述：给定一个整数数组，找到一个具有最小和的子数组。返回其最小和
样例：
    样例 1
        输入：[1, -1, -2, 1]
        输出：-3
    样例 2
        输入：[1, -1, -2, 1, -4]
        输出：-6
'''

class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def minSubArray(self, nums):
        # write your code here
        sum = 0
        minSum, maxSum = nums[0], 0
        for num in nums:
            sum += num
            if sum - maxSum < minSum:
                minSum = sum - maxSum
            if sum > maxSum:
                maxSum = sum
        return minSum