# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p_a = headA
        p_b = headB
        while p_a != p_b:
            if p_a == None:
                p_a = headB
            else:
                p_a = p_a.next
            if p_b == None:
                p_b = headA
            else:
                p_b = p_b.next
        return p_a

        #Loop will only exit if p_a == p_b or if it is none 