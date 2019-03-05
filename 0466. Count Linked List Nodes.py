# coding=utf-8
'''
描述：计算链表中有多少个节点
样例
    样例  1:
        输入:  1->3->5->null
        输出: 3        
        样例解释: 
        返回链表中结点个数，也就是链表的长度.
    样例 2:
        输入:  null
        输出: 0        
        样例解释: 
        空链表长度为0
'''

class Solution:
    """
    @param head: the first node of linked list.
    @return: An integer
    """
    def countNodes(self, head):
        # write your code here
        n = 0
        ptr = head
        while ptr != None:
            n = n + 1
            ptr = ptr.next
        return n