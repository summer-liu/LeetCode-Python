# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if head == None:
            return None
        p = head
        while p:
            newNode = RandomListNode(p.label)
            newNode.next = p.next
            p.next = newNode
            p = p.next.next
            
        p = head
        while p:
            if p.random:
                p.next.random = p.random.next
            p = p.next.next
         
        newhead = head.next   
        pold = head
        pnew = newhead
        while pnew.next:
            pold.next = pnew.next
            pold = pold.next
            pnew.next = pold.next
            pnew = pnew.next
        pnew.next = None
        pold.next = None
        return newhead
            
            
        