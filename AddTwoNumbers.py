# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        head = ListNode(0)
        curr = head
        carry = 0 
        while l1 and l2:
            sum = l1.val + l2.val + carry
            carry = sum/10
            curr.next = ListNode(sum%10)
            l1 = l1.next
            l2 = l2.next
            curr = curr.next
        while l1:
            sum = l1.val + carry
            carry = sum/10
            curr.next = ListNode(sum%10)
            l1 = l1.next
            curr = curr.next
        while l2:
            sum = l2.val + carry
            carry = sum/10
            curr.next = ListNode(sum%10)
            l2 = l2.next
            curr = curr.next
        if carry > 0:
            curr.next = ListNode(carry)
        return head.next

   
            
        
        