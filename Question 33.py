# Concept name : Binary Tree - DFS

# Question : Maximum Depth of Binary Tree

#            Given the root of a binary tree, return its maximum depth.        
#            A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
              
#                         Example 1:
                        
#                         Input: root = [3,9,20,null,null,15,7]
#                         Output: 3

# Solution : 

class Solution(object):
    def maxDepth(self, root):
        if root is None:
            return 0
        lh=self.maxDepth(root.left)
        rh=self.maxDepth(root.right)
        return 1+max(lh,rh)
             
# Explanation: 1. If the root is None, return 0 (empty tree has depth 0).
#              2. Recursively find the depth of left and right subtrees.
#              3. Take the maximum of the two depths and add 1 (for the current root node).
#              4. Return the computed depth.
