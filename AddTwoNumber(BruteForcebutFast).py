# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not l1 and not l2:
            return None
        dummy = res = ListNode()
        carry,add = 0,0
        while (l1.next and l2.next):
            add = l1.val+l2.val+carry
            res.val = add-10 if add >9 else add
            carry = 1 if add>9 else 0

            l1=l1.next
            l2=l2.next
            res.next = ListNode()
            res = res.next
        
        add = l1.val+l2.val+carry
        res.val = add-10 if add >9 else add
        carry = 1 if add>9 else 0   
        l1=l1.next
        l2=l2.next

        if l1 or l2:
            res.next= l1 if l1 else l2
            res = res.next

        while carry and res.next:
            add = res.val+carry
            res.val = add-10 if add >9 else add
            carry = 1 if add>9 else 0
            res = res.next

        if l1 or l2:
            add = res.val+carry
            res.val = add-10 if add >9 else add
            carry = 1 if add>9 else 0

        if carry:
            res.next = ListNode()
            res.next.val =1
        return dummy
