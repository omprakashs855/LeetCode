# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur_l1 = l1
        cur_l2 = l2
        dec = 1
        A, B = 0,0
        
        while True:
            if cur_l1 == None and cur_l2 == None:
                break
            if cur_l1 != None:
                A += int(cur_l1.val)*dec
                cur_l1 = cur_l1.next
            if cur_l2 != None:
                B += int(cur_l2.val)*dec
                cur_l2 = cur_l2.next
            dec *= 10
        
        C = A+B
        head = ListNode()
        curr = head

        if C == 0:
            return ListNode(0)

        while C>0:
            curr.next = ListNode(val=C%10)
            curr = curr.next
            C = C//10
        
        return head.next
            



            
            
        