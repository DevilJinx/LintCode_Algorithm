# coding=utf-8
'''
描述：给定一个整数数组，找到一个具有最大和的子数组，返回其最大和
样例：
    样例1:
        给出数组[−2,2,−3,4,−1,2,1,−5,3]，符合要求的子数组为[4,−1,2,1]，其最大和为6
    样例2:
        给出数组[1,2,3,4]，符合要求的子数组为[1,2,3,4]，其最大和为10

挑战：要求时间复杂度为O(n)
'''

class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, nums):
        # write your code here
        min_sum, max_sum = 0, -sys.maxsize
        prefix_sum = 0
        
        for num in nums:
            prefix_sum += num
            max_sum = max(max_sum, prefix_sum - min_sum)
            min_sum = min(min_sum, prefix_sum)
        return max_sum

'''
使用前缀和的方法，计算每个位置为结尾的子数组的最大值是多少
'''