from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
            
        queue = deque([root])
        ans = []

        while len(queue) > 0:
            new_level = []
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                new_level.append(node.val)

                for child in [node.left, node.right]:
                    if child is not None:
                        queue.append(child)

            ans.append(new_level)
        
        return ans
