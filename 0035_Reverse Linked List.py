# coding=utf-8
'''
描述：翻转一个链表
样例：
    样例1:
        对于链表 1->2->3, 翻转链表为 3->2->1
    样例2:
        对于链表 1->2->3->4, 翻转链表为 4->3->2->1
挑战：在原地一次翻转完成
'''

class Solution:
    """
    @param head: n
    @return: The new head of reversed linked list.
    """
    def reverse(self, head):
        # write your code here
        curt = None
        while head != None:
            temp = head.next
            head.next = curt
            curt = head
            head = temp
        return curt