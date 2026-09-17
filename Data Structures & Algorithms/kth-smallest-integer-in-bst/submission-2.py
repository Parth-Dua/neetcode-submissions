# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        lst = []
        # In order traversal -> order of elements in BST
        def helper(root): 
            nonlocal lst
            if not root: 
                return

            if len(lst) == k: 
                return
            
            helper(root.left)
            lst.append(root.val)
            helper(root.right)


        helper(root)
        return lst[k-1]

    