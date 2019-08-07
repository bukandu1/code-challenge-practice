
class LinkedList():
    def __init__(self, head_node=None):
        self.head = head_node
        self.tail = head_node

class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


def merge_two_linked_lists(LL1, LL2):
    if not LL1 or not LL2:
        if not LL1: 
            return LL2
        else:
            return LL1

a = Node(1)
b = Node(4)
c = Node(8)

a.next = b
b.next = c

d = Node(1)
e = Node(2)
f = Node(7)

d.next = e
e.next = f

g = Node(8)

LL1 = LinkedList(a)
LL2 = LinkedList(d)


