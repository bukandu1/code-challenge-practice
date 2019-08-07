
class LinkedList():
    def __init__(self, head_node=None):
        self.head = head_node
        self.tail = head_node

    def traverse(self):
        current = self.head
        while current:
            print(current.value)
            current = current.nextLL

class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


def merge_two_linked_lists(LL1, LL2):
    if not LL1.head or not LL2.head:
        if not LL1: 
            return LL2.head
        else:
            return LL1.head

    currA = LL1.head
    currB = LL2.head
    LL3 = LinkedList(Node(0))

    #while currA  and currB
    while currA and currB:
        #if currA <= currB:
            #add to currA to LL3

        if currA.value <= currB.value:
            LL3.tail.next = currA
            LL3.tail = currA
            currA = currA.next

        else:
        #else:
            #add to currB to LL3
            if not LL3.head:
                LL3.head = currB
                LL3.tail = currB
            #update pointer to currB
            LL3.tail.next = currB
            LL3.tail = currB
            currB = currB.next

    #handle when length of LL different list
    if currA:
        while currA:
            #traverse LL1 and add to LL3
           LL3.tail.next = currA
           LL3.tail = currA
           currA = currA.next

    else:
        #traverse LL2 and add to LL3
        while currB:
            LL3.tail.next = currB
            LL3.tail = currB
            currB = currB.next

    return LL3.head.next



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


