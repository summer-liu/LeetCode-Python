# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    # def addTwoNumbers(self, l1, l2):
    #     head = ListNode(0)
    #     curr = head
    #     carry = 0 
    #     while l1 and l2:
    #         sum = l1.val + l2.val + carry
    #         carry = sum/10
    #         curr.next = ListNode(sum%10)
    #         l1 = l1.next
    #         l2 = l2.next
    #         curr = curr.next
    #     while l1:
    #         sum = l1.val + carry
    #         carry = sum/10
    #         curr.next = ListNode(sum%10)
    #         l1 = l1.next
    #         curr = curr.next
    #     while l2:
    #         sum = l2.val + carry
    #         carry = sum/10
    #         curr.next = ListNode(sum%10)
    #         l2 = l2.next
    #         curr = curr.next
    #     if carry > 0:
    #         curr.next = ListNode(carry)
    #     return head.next
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        p = dummy
        sum = 0
        while l1 is not None or l2 is not None:
            sum //= 10
            if l1 is not None:
                sum += l1.val
                l1 = l1.next
            if l2 is not None:
                sum += l2.val
                l2 = l2.next
            p.next = ListNode(sum % 10)
            p = p.next
        if (sum //10 == 1):
            p.next = ListNode(1)
        return p.next
   
            
        
        