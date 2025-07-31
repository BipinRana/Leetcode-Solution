# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """

        if not head or not head.next:
            return True

        slow = fast = head
   
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
  
        right = None
        curr = slow.next
        while curr:
            temp = curr.next
            curr.next = right
            right = curr
            curr = temp

        while right:
            if right.val != head.val:
                return False
            right= right.next
            head = head.next
        
        return True

    
        
     

