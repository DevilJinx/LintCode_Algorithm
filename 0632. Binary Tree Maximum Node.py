# coding=utf-8
'''
描述：在二叉树中寻找值最大的节点并返回

样例
    样例 1：
        输入：
            1
           /   \
         -5     3
         / \   /  \
        1   2 -4  -5 

            输出： 值为3的节点
            样例解释：
                返回值最大的节点
    
    样例 2：
        输入：
            10
           /   \
          -5     2
         / \   /  \
        0   3 -4  -5 
            
            输出： 值为10的节点
            样例解释：
            返回值最大的节点
'''

class Solution:
    """
    @param: root: the root of tree
    @return: the max node
    """
    def maxNode(self, root):
        # write your code here
        if root is None:
            return root
        
        left = self.maxNode(root.left)
        right = self.maxNode(root.right)
        return self.max(root, self.max(left, right))
        
    def max(self, a, b):
        if a is None:
            return b
        if b is None:
            return a
        if a.val > b.val:
            return a
        return b