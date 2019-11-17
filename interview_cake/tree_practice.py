class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.children = []
        self.left = None
        self.right = None

    def inorder_search(self, root):
        """
        L branch, current node, R branch
        """
        if root:
            self.inorder_search(root.left)
            print(root.value)
            self.inorder_search(root.right)
    
    def preorder_search(self, root):
        """
        Visit the current node before visits children
        Root always the first visited
        10
        5
        9
        18
        20
        3
        7
        """
        if root:
            print(root.value)
            self.preorder_search(root.left)
            self.preorder_search(root.right)

    #         10
    #         /\
    #     5     20
    #   /\        /\
    #  9   18     3  7
# Quick and dirty binary tree creation
root = Node(10)
left1 = Node(5)
right1 = Node(20)
root.left = left1
root.right = right1
left1.left = Node(9)
left1.right = Node(18)
right1.left = Node(3)
right1.right = Node(7)

print(root.left.left.value, root.right.value)

root.inorder_search(root)
print("~~~~~~~~~~~~~~~~~~~~~~")
root.preorder_search(root)


