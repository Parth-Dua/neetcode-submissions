# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        ans = None 

        def helper(root): 
            nonlocal ans 
            # For a node to be LCA, p is to be in one subtree and q in another 
            if not root: 
                return 

            if (root.val <= p.val and root.val >= q.val) or (root.val >= p.val and root.val <= q.val): 
                ans = root 
                return

            if root.val < p.val: 
                helper(root.right)
            else: 
                helper(root.left)

            return

        helper(root)
        return ans 
                

            