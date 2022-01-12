class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        try:
            p = head
            q = head.next
            while p != q:
                p = p.next
                q = q.next.next
            return True 
        except:
            return False