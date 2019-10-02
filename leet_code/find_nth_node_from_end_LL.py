# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        To remove: 
        while  counter != n:
            move to next node
            
        when nth node found, remove
            prev.next = current.next
            
        """
        if not head:
            return None
        
        #if first node needs to be removed
        if n == 0:
            return head.next
        
        self.prev_node = head
        self.current_node = head
        self.length = -1
        index = 0
        
        find_helper(self.prev_node, self.current_node, index, n)
        
        # while counter != n:
        #     prev = current
        #     current = current.next
        #     counter += 1
        
        
        self.prev_node.next = self.current_node.next
        
        return head
        
    def find_helper(self, prev, current, index, n):
        if not current.next:
            self.length = index
            return self.length
        else:
            if self.length - n - 1 == index:
                self.prev_node = prev
                self.current_node = current
            return find_helper(current, current.next, index+1)