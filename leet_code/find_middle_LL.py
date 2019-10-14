"""
Given the head of a non-empty, singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.

1->4->2->7->5 returns 2

"""
class Node():
    def __init__(self, value):
        self.next = None
        self.value = value


class Solution:
    def find_middle(self, head):
        #create a dictionary to store items in
        node_dict = dict()
        current = head
        length = 0
        
        if not head:
            return 0
        
        if not head.next:
            return head

        while(current):
            #store into dictionary
            node_dict[length] = current
            current = current.next
            length += 1

        mid = length//2
        
        # if length % 2 == 0:
        #     mid += 1

        print(length, mid)
        return node_dict[mid]

n1 = Node(1)
n2 = Node(4)
n3 = Node(2)
n4 = Node(7)
n5 = Node(5)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

# print(n2.value, n5.value)

sol = Solution()
print(sol.find_middle(n1).value)
