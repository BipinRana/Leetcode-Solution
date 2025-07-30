# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        # Create a dummy node to handle edge cases (e.g., removing the head)
        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = dummy
        
        # Move fast pointer n steps ahead
        for _ in range(n):
            fast = fast.next
            
        # Move both pointers until fast reaches the end
        while fast.next:
            slow = slow.next
            fast = fast.next
            
        # Slow is now at the node before the one to remove
        slow.next = slow.next.next
        
        return dummy.next
