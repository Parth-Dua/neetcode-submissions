# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        
        # recursion aint gonna store the actual answer
        # it will give back the maximum from that path


        ans = -float("inf")

        def helper(root) :
            nonlocal ans 
            if not root: 
                return 0 

            left = helper(root.left)
            right = helper(root.right)
        
            incl_root_max_sum = root.val + max(left, right)
            ans = max(ans, incl_root_max_sum)

            ans = max(ans, root.val + left + right )

            ans = max(ans, root.val)

            return max(root.val, incl_root_max_sum)

        helper(root)
        return ans 