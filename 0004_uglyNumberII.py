'''
描述：
    设计一个算法，展出只含素因子2, 3, 5的第n小的数
    符合条件的数如：1, 2, 3, 4, 5, 6, 8, 9, 10, 12...
样例：
    如果n = 9，返回10
挑战：
    要求时间复杂度为O(nlogn)或者O(n)
'''

class Solution:
    """
    @param n: An integer
    @return: the nth prime number as description.
    """
    def nthUglyNumber(self, n):
        # write your code here
        ugly = []
        ugly.append(1)
        num_2 = 0
        num_3 = 0
        num_5 = 0
        for i in range(1,n):
            ugly.append(min(ugly[num_2]*2,ugly[num_3]*3,ugly[num_5]*5))
            if(ugly[i] / ugly[num_2] == 2):
                num_2 += 1
            if(ugly[i] / ugly[num_3] == 3):
                num_3 += 1
            if(ugly[i] / ugly[num_5] == 5):
                num_5 += 1
        return ugly[-1]