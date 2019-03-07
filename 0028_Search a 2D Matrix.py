# coding=utf-8
'''
描述：写出一个高效的算法来搜索 m × n矩阵中的值。
    这个矩阵具有以下特性：
        每行中的整数从左到右是排序的。
        每行的第一个数大于上一行的最后一个整数。
样例：
    样例  1:
        输入: [[5]],2
        输出: false
        样例解释: 没有包含，返回false。
    样例 2:
        输入:  
            [
                [1, 3, 5, 7],
                [10, 11, 16, 20],
                [23, 30, 34, 50]
            ],3
        输出: true
        样例解释: 包含则返回true。
挑战：O(log(n) + log(m)) 时间复杂度
'''
'''
思路0：从左下角到右上角开始查找，经典答案
(101 ms)
'''
class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if not matrix or not len(matrix[0]) :
            return False
        i = 0
        j = len(matrix[0]) - 1
        while i < len(matrix) and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            else:
                i += 1
        return False

'''
思路1：第一次二分搜索出在哪一行，第二次二分搜索直接确定存在
(101 ms)
'''
class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if not matrix or not len(matrix[0]) :
            return False
        left, right = 0, len(matrix) - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[mid][0] > target:
                right = mid - 1
            elif matrix[mid][0] < target:
                left = mid + 1
            else:
                return True
        
        x = left - 1
        print('--', x)
        left, right = 0, len(matrix[0]) - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[x][mid] > target:
                right = mid - 1
            elif matrix[x][mid] < target:
                left = mid + 1
            else:
                return True
        return False

'''
思路2：把矩阵从左到右、从上到下连起来就是一个递增的数组，可以用二分搜索来查找。现在只要找出数组下标到矩阵的的映射关系就可以了：
    i > [i // n][i % n]，其中i是数组中的下标，n是矩阵的宽
(101 ms)
'''
class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if not matrix or not len(matrix[0]) :
            return False
        m, n = len(matrix), len(matrix[0])
        l, h = 0, n * m - 1
        while l <= h:
            mid = l + (h - l) // 2
            if matrix[mid // n][mid % n] == target:
                return True
            elif matrix[mid // n][mid % n] < target:
                l = mid + 1
            else:
                h = mid - 1
        return False