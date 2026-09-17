# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        

        def helper(root, max_in_path): 
            if not root: 
                return 0

            count = 0

            if root.val >= max_in_path: 
                # YES, good node 0 -> add to count
                count+=1

            good_nodes_in_left_subtree = helper(root.left, max(root.val, max_in_path))
            good_nodes_in_right_subtree = helper(root.right, max(root.val, max_in_path))

            return count + good_nodes_in_left_subtree + good_nodes_in_right_subtree

        return helper(root, -float("inf"))
        