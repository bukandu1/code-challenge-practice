
class LinkedList():
    def __init__(self, head_node=None):
        self.head = head_node
        self.tail = head_node

class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


def merge_two_linked_lists(LL1, LL2):
    if not LL1.head or not LL2.head:
        if not LL1: 
            return LL2
        else:
            return LL1

    #while currA  and currB
        #if currA <= currB:
            #add to currA to LL3
            #update pointer to currA
        #else:
            #add to currB to L:3
            #update pointer to currB

    #handle when length of LL different list
    #if LL1:
        #traverse LL1 and add to LL3
    #else:
        #traverse LL2 and add to LL3LL1



#Test Cases
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
LL4 = LinkedList()


