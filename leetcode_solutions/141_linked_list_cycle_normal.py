class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        p = q = head
        while p != None and q != None and q.next != None:
            p = p.next
            q = q.next.next
            
            if p == q:
                return True 
        
        return False