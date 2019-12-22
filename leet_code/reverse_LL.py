
# Reverse a singly linked list

class Node():
    def __init__(self, value):
        self.value = value 
        self.next = None

class Solution:
    """
    none <-1 2->3->4->none
           c
        prev
    1->none
    none

    prev = none
    current = head
    next = current.next

    while current:
        current.next = prev
        prev = current
        current = next
        
    
    """
    def reverseLinkedList(self, head):
        self.
        
