# coding=utf-8
'''
描述：合并两个排序的整数数组A和B变成一个新的数组。新数组也要有序
样例：
    样例  1:
        输入: A=[1], B=[1]
        输出:[1,1]   
        样例解释: 
        返回合并后的数组。
    样例 2:
        输入: A=[1,2,3,4], B=[2,4,5,6]
        输出: [1,2,2,3,4,4,5,6]   
        样例解释: 
        返回合并后的数组。
挑战：你能否优化你的算法，如果其中一个数组很大而另一个数组很小？
'''

'''
简单操作：
(101 ms)
'''
class Solution:
    """
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """
    def mergeSortedArray(self, A, B):
        # write your code here
        A = A + B
        A.sort()
        return (A)

'''
复杂操作：
(101 ms)
'''
class Solution:
    """
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """
    def mergeSortedArray(self, A, B):
        # write your code here
        C = []
        alen = len(A)
        blen = len(B)
        i = 0
        j = 0
        while i < alen or j < blen:
            if (i < alen and j < blen):
                if A[i] <= B[j]:
                    C.append(A[i])
                    i += 1
                else:
                    C.append(B[j])
                    j += 1
            if i == alen and j < blen:
                C.append(B[j])
                j += 1
            if i < alen and j == blen:
                C.append(A[i])
                i += 1
        return C