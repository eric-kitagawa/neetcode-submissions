from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        queue = deque([root])
        ans = []
        # Each iteration of the while loop represents one level order
        while len(queue) > 0:
            # This for loop is traversing that level
            n = len(queue)
            ans.append(queue[0].val)
            for _ in range(n):
                node = queue.popleft()
                for child in [node.right, node.left]:
                    if child:
                        queue.append(child)
        
        return ans