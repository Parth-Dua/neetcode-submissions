# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def helper(r1, r2):
            
            if (not r1 and not r2) :
                return True

            if (not r1 and r2 ) or (not r2 and r1): 
                return False

            left_res = helper(r1.left, r2.left)
            right_res = helper(r1.right, r2.right)

            if r1.val == r2.val and left_res and right_res: 
                return True
            else: 
                return False

        return helper(p,q)


