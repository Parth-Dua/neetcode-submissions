# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root: 
            return []

        queue = deque()

        queue.append(root)
        ans  = []

        while queue: 
            level_size = len(queue)
            curr_level = []
            
            for _ in range(level_size): 
                el = queue.popleft()
                
                curr_level.append(el.val)

                if el.left: 
                    queue.append(el.left)
                if el.right: 
                    queue.append(el.right)

            ans.append(curr_level.copy())
        
        return ans 
