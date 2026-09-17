# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        ans = True

        def helper(root): 
            nonlocal ans
            if not root:
                return 0
            
            left_height = helper(root.left)
            right_height = helper(root.right)

            ans = ans and (abs(left_height-right_height) <= 1 )

            return 1 + max(left_height,right_height)
        
        helper(root)
        return ans



