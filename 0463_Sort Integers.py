# coding=utf-8
'''
描述：给一组整数，按照升序排序，使用选择排序，冒泡排序，插入排序或者任何 O(n²) 的排序算法。
样例：
    样例  1:
        输入:  [3, 2, 1, 4, 5]
        输出:  [1, 2, 3, 4, 5]
        
        样例解释: 
        返回排序后的数组。

    样例 2:
        输入:  [1, 1, 2, 1, 1]
        输出:  [1, 1, 1, 1, 2]
        
        样例解释: 
        返回排好序的数组。
'''

'''
冒泡法排序:遍历数组，把当前数字的后面所有的数字都遍历一遍，遇到小的跟当前数字交换，这样遍历的过程中，所有大的数字就像气泡一样都到数组的后面去了
(352 ms)
'''
class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers(self, A):
        # write your code here
        for i in range(len(A) - 1):
            for j in range(i + 1, len(A)):
                if A[i] >= A[j]:
                    A[i], A[j] = A[j], A[i]
                    j += 1
        return (A)

'''
插入排序：有一个已经有序的数据序列，要求在这个已经排好的数据序列中插入一个数，但要求插入后此数据序列仍然有序，这个时候就要用到一种新的排序方法——插入排序法,插入排序的基本操作就是将一个数据插入到已经排好序的有序数据中，从而得到一个新的、个数加一的有序数据
(252 ms)
'''
class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers(self, A):
        # write your code here
        for i in range(1, len(A)):
            save = A[i]
            j = i
            while j > 0 and A[j - 1] > save:
                A[j] = A[j - 1]
                j -= 1
            A[j] = save
        return (A)

'''
选择排序：思路是遍历数组，对于当前位置i，我们定义一个变量min_idx，用来记录当前位置往后的最小值的坐标，我们通过遍历之后所有的数字来找到最小值的坐标，然后交换A[i]和A[min_idx]即可
(101 ms)
'''
class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers(self, A):
        # write your code here
        i = 0
        j = len(A) - 1
        self.quick_sort(A, i, j)
    def quick_sort(self, A, low, high):
        if low < high:
            i = low
            j = high
            tmp = A[low]
            while i < j:
                while i < j and A[j] >= tmp:
                    j -= 1
                A[i] = A[j]
                while i < j and A[i] < tmp:
                    i += 1
                A[j] = A[i]
            A[i] = tmp
            self.quick_sort(A, low, i - 1)
            self.quick_sort(A, i + 1, high)