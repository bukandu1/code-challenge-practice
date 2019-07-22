



# 7/13/19 Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#      5
#    /  \
#    3   4
  /  \   /  \
#2   1   6   7
#        /\
#       10  15


class Solution:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        to_visit_list = []
        depth_set = set()
        
        if not root:
            return 0
            
        depth = 1
        to_visit_list.append((root, depth))
        #print(root.val, depth)

        #while items in to_visit list
        while to_visit_list:
            #remove last item in list to review
            current, depth = to_visit_list.pop()

            #is a leaf?
            if not current.right and not current.left: 
                #store into depth set
                depth_set.add(depth)
                #print("Set contains", depth_set)
            else:
                if current.right: 
                    to_visit_list.append((current.right, depth + 1))
                if current.left: 
                    to_visit_list.append((current.left, depth + 1))
        
        return max(depth_set)
        return max(depth_set)
                
        
        