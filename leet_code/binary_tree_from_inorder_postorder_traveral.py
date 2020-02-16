# 106. Construct Binary Tree from Inorder and Postorder Traversal 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        # base case: if inorder == null: return null (L and R trees do not exist)
        # Determine root from postorder
        # Determine L and R subtrees from inorder
        # create node from root
        # assign node.left to left tree and node.right to right tree
        # return root
        
        if not inorder:
            return None
        else:
            rootVal = postorder[-1]
            rootNode = TreeNode(rootVal)
            
            for i in range(len(inorder)):
                if inorder[i] == rootVal:
                    rootIndex = i
                    break
            
            # default if no L or no R subtree
            rightInST, leftInST = [], []
            
            if rootIndex + 1 < len(inorder):
                # right tree found
                rightInST = inorder[rootIndex + 1:]
            
            if rootIndex > 0:
                # left tree found
                leftInST = inorder[0:rootIndex]
            
            rightPostST = [x for x in postorder if x in rightInST]
            leftPostST = [x for x in postorder if x in leftInST]
            
            rootNode.right = self.buildTree(rightInST, rightPostST)
            rootNode.left = self.buildTree(leftInST, leftPostST)
        
        return rootNode
            