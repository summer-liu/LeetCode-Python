# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if head == None or head.next == None or head.next.next == None:
            return head
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        head1 = head
        head2 = slow.next
        slow.next = None
        
        dummy = ListNode(0)
        dummy.next = head2
        p = head2.next
        head2.next = None
        while p:
            tmp = p
            p = p.next
            tmp.next = dummy.next
            dummy.next = tmp
        head2 = dummy.next 
        
        p1 = head1
        p2 = head2
        while p2:
            tmp1 = p1
            tmp2 = p2
            p1 = p1.next
            p2 = p2.next
            tmp2.next = tmp1.next
            tmp1.next = tmp2
    
    
        
        
            
    
            
      