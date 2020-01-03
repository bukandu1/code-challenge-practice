# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        """
        Following the guidelines we lay out above, we can implement the function as follows:

        First, we swap the first two nodes in the list, i.e. head and head.next;
        Then, we call the function self as swap(head.next.next) to swap the rest of the list following              the first two nodes.
        Finally, we attach the returned head of the sub-list in step (2) with the two nodes swapped in              step (1) to form a new linked list.
        """
        
        i = head
        j = head.next
        
        dummy = ListNode(-1)
        dummy.next = j
        
        while i and j:
            temp = i
            i.next = j.next
            j.next = temp
            
            i = i.next
            j = i.next.next
            
        return dummy.next