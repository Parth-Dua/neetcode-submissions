# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Easy way = level order traversal - O(n) and O(n)
        if not root: 
            return []

        queue = deque()
        queue.append(root)
        ans = []

        while len(queue)> 0: 
            last_element = None
            level_size = len(queue)

            # Process the full level
            for i in range(level_size) :
                element = queue.popleft()
                last_element = element.val

                # Add the children to the queue
                if element.left: 
                    queue.append(element.left)
                if element.right: 
                    queue.append(element.right)

            ans.append(last_element)
            
        return ans

