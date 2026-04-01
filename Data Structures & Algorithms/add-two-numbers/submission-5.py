# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0

        dummy = ListNode()
        res = dummy

        while (l1 and l2):
            if (l1.val + l2.val + carry >= 10):
                r = (l1.val + l2.val) % 10
                res.next = ListNode(r + carry)
                carry = 1
            else:
                res.next = ListNode(l1.val + l2.val + carry)
                carry = 0

            res = res.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            if (l1.val + carry >= 10):
                res.next = ListNode(l1.val - 10 + carry)
                carry = 1
            else:
                res.next = ListNode(l1.val + carry)
                carry = 0
            res = res.next
            l1 = l1.next

        while l2:
            if (l2.val + carry >= 10):
                res.next = ListNode(l2.val - 10 + carry)
                carry = 1
            else:
                res.next = ListNode(l2.val + carry)
                carry = 0
                
            res = res.next
            l2 = l2.next

        while carry > 0:
            res.next = ListNode(carry)
            carry = 0
    
        return dummy.next