# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        current = head
        seen = set()
        prev = current
        
        while current:
            if current.val not in seen:
                seen.add(current.val)
                prev = current
                
            else:
                prev.next = current.next
                
            current = current.next
            
        return head

#Runtime: 44 ms, faster than 92.13% of Python3 online submissions for Remove Duplicates from Sorted List.
#Memory Usage: 13.8 MB, less than 6.45% of Python3 online submissions for Remove Duplicates from Sorted List.