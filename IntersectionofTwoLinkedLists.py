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
        if (not headA) or (not headB):
            return none
            
        left,right = headA , headB
        
        while left != right:
            left = left.next if left else headB
            right = right.next if right else headA
        return left
