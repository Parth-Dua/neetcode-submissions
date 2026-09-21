# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def helper(node, max_val_from_root_to_node): 

            if not node: 
                return 0 

            count = 0 
            if node.val >= max_val_from_root_to_node: 
                count+=1 
            
            count = count + helper(node.left, max(node.val, max_val_from_root_to_node)) + helper(node.right, max(node.val, max_val_from_root_to_node))

            return count

        return helper(root, root.val)