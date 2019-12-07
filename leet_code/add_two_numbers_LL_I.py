# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(-1)
        current = head
        
        i = l1
        j = l2
        digit_carry = 0
        
        while i or j:
            if not i:
                x = 0
            else:
                x = i.val
            if not j:
                y = 0
            else:
                y = j.val
                
            sum = x + y + digit_carry
            current.next = ListNode(sum % 10)
            digit_carry = sum // 10
            print(digit_carry)
            
            current = current.next
            
            if i:
                i=i.next
            if j:
                j=j.next
            
        """while i:
            sum = i.val + digit_carry
            current.next = ListNode(sum)
            current = current.next
            digit_carry = 0
            i = i.next   
            
        while j:
            sum = j.val + digit_carry
            current.next = ListNode(sum)
            current = current.next
            digit_carry = 0
            j = j.next
        """
        if digit_carry > 0:
            current.next = ListNode(digit_carry)
        return head.next