# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        queue = deque()
        queue.append(root)

        ans = []

        # BFS

        while len(queue)!=0 :
            level = []

            level_size = len(queue)

            for i in range(level_size): 
                
                el = queue.popleft()
                level.append(el.val)

                # Add the elements children to the list and to the queue
                if el.left: 
                    queue.append(el.left)
                if el.right: 
                    queue.append(el.right)

            ans.append(level)

        
        return ans 
            
