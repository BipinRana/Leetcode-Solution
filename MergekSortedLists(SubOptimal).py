# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        if not lists:
            return None
         
        head = dummy = ListNode()
        
        for i in range(len(lists)-1,-1,-1):
            if not lists[i]:
                continue
            if not head.next:
                head.next = lists[i]
                continue
            
            temp = lists[i]
            
            while head.next and temp:
                if head.next and head.next.val>temp.val:
                    prev = head.next
                    prev2 = temp.next
                    temp.next = None
                    head.next = temp
                    head = head.next
                    head.next = prev
                    temp = prev2
                else:
                    head = head.next
            if temp:
                head.next = temp
            head = dummy
        return dummy.next


        
