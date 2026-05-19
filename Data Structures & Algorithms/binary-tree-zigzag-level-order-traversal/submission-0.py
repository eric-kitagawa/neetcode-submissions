from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        queue = deque([root])
        ans = []
        right_to_left = False

        while len(queue) > 0:
            n = len(queue)
            level = []

            for _ in range(n):
                node = queue.popleft()
                level.append(node.val)
                for child in [node.left, node.right]:
                    if child is not None:
                        queue.append(child)
            if right_to_left:
                level.reverse()
            
            ans.append(level)
            right_to_left = not right_to_left
        
        return ans