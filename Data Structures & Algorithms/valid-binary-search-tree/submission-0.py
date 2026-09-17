# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def helper(root, max_in_left_subtree, min_in_right_subtree) :

            if not root: 
                return True
            
            # It is isValidBST

            if root.val > max_in_left_subtree and root.val < min_in_right_subtree: 
                ans = True
        
            else: 
                ans = False

            
            left_subtree_bst_check = helper(root.left, max_in_left_subtree, root.val
)
            right_subtree_bst_check = helper(root.right, root.val, min_in_right_subtree)

            return ans and left_subtree_bst_check and right_subtree_bst_check

        return helper(root, -float("inf"), float("inf"))


            