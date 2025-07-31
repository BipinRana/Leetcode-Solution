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

        dummy = slow = fast = head
        slow_list = []
        fast_list = []
        while fast and fast.next:
            slow_list.append(slow.val)
            fast_list.append(fast.val)
            fast_list.append(fast.next.val)
            slow = slow.next
            fast = fast.next.next
        
        if fast:
            fast_list.append(fast.val)
            slow_list.append(slow.val)
        
        if fast_list[-1:-len(slow_list)-1:-1] == slow_list:
            return True
        else:
            return False
