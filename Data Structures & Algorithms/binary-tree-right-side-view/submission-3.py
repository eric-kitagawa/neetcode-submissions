from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        levels = []
        res = []
        def dfs(root, depth):
            if not root:
                return
            
            if depth == len(levels):
                levels.append([])

            levels[depth].append(root.val)
            
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)
        
        dfs(root, 0)
        
        for level in levels:
            res.append(level.pop())
            
        return res