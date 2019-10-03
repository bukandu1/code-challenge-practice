# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Runtime: 32 ms, faster than 97.12% of Python3 online submissions for Remove Nth Node From End of List.
# Memory Usage: 13.8 MB, less than 6.06 % of Python3 online submissions for Remove Nth Node From End of List.

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
            i and j pointers
            Move j n away (so that i and j are n apart)
            Move i and j pointers until j == null
            remove i node
            return head
        """
        if not head:
            return None

        i = head
        j = head

        for num in range(n):
            j = j.next

        while j:
            i_prev = i
            i = i.next
            j = j.next

        #print("i = ", i.val)

        #if the first node is still the head, return the second node as the head
        if i == head:
            return head.next
        elif not i:
            i_prev.next = None
        else:
            i_prev.next = i.next

        return head
