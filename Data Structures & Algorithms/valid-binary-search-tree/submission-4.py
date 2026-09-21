# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        

        def helper(root, left_boundary, right_boundary ): 

            if not root: 
                return True 
                
            if root.val <= left_boundary or root.val>= right_boundary: 
                return False 

            return helper(root.left, left_boundary, root.val) and helper(root.right, root.val, right_boundary) 
        
        return helper(root, float("-inf"), float('inf'))