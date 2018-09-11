'''
描述：
    在数组中找到第k大的元素
样例：
    给出数组[9， 3， 2， 4， 8]，第三大的元素是4
    给出数组[1， 2， 3， 4， 5]，第一大的元素是5，第二大的元素是4，第三大的元素是3，以此类推
挑战：
    要求时间复杂度为O(n)，空间复杂度为O(1)
'''

class Solution:
    # @param k & A a integer and an array
    # @return ans a integer
    def kthLargestElement(self, k, A):
        if not A or k < 1 or k > len(A):
            return None
        return self.partition(A, 0, len(A) - 1, len(A) - k)
        
    def partition(self, nums, start, end, k):
        """
        During the process, it's guaranteed start <= k <= end
        """
        if start == end:
            return nums[k]
            
        left, right = start, end
        pivot = nums[(start + end) // 2]
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left, right = left + 1, right - 1
                
        # left is not bigger than right
        if k <= right:
            return self.partition(nums, start, right, k)
        if k >= left:
            return self.partition(nums, left, end, k)
        
        return nums[k]