class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        my_list = []
        while head:
            my_list.append(head.val)
            head = head.next
        p_1 = 0 
        p_2 = len(my_list) - 1
        
        while p_1 < p_2:
            if my_list[p_1] != my_list[p_2]:
                return False
            p_1 += 1
            p_2 -= 1
        return True 
