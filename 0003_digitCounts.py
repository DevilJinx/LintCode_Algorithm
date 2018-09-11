class Solution:
    """
    @param: : An integer
    @param: : An integer
    @return: An integer denote the count of digit k in 1..n
    """

    def digitCounts(self, k, n):
        L = ''.join([str(i) for i in range(n+1)])
        c = L.count(str(k))
        return c