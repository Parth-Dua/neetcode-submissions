# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        lca = None
        #Returns the exact node
        def helper(root):
            nonlocal lca

            if not root: 
                return None

            # p is in the left and q in right
            if (p.val <= root.val and q.val>= root.val) or (q.val <= root.val and p.val>= root.val): 
                lca = root
                return
            
            # Search left and right
            # if smaller go left
            if p.val < root.val and q.val < root.val: 
                helper(root.left)
            # else go right
            else: 
                helper(root.right)
        
        helper(root)
        return lca    

            #Algo: Find one of them, and then on the way of recursion back, check their children, and when w\e find the other of p and q, that root is the lowestCommonAncestor

            # Found p now, find q when going upwards
            # All the ancestors are in the stack
            


             

        
        return helper( root )

