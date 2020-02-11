class Queue():
    def __init__(self):
        self.reverse_lst = []
        self.inorder_lst = []

    def enqueue(self, value):
            self.reverse_lst.append(value)

    def deque(self):
        if not self.reverse_lst and not self.inorder_lst:
            return "Nothing to deque"

        elif not self.inorder_lst:
            while self.reverse_lst:
                temp = self.reverse_lst.pop()
                self.inorder_lst.append(temp)
        
        return self.inorder_lst.pop()

        
    def print(self):
        print(self.reverse_lst, self.inorder_lst)


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.print()
print('Deque value', q.deque())
q.print()
print('Deque value', q.deque())
q.print()
q.enqueue(5)
q.print()
print('Deque value', q.deque())
q.print()
print('Deque value', q.deque())
q.print()
print('Deque value', q.deque())
q.print()
print('Deque value', q.deque())
q.print()
