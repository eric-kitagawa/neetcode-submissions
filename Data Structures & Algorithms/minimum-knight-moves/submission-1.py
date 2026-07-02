from collections import deque
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        x, y = abs(x), abs(y)
        if x == 0 and y == 0:
            return 0
            
        def get_neighbors(node):
            cx, cy, move_num = node
            x_delta = [1, 2, 2, 1, -1, -2, -2, -1]
            y_delta = [-2, -1, 1, 2, 2, 1, -1, -2]
            res = []
            
            for i in range(len(x_delta)):
                neighbor_x = cx + x_delta[i]
                neighbor_y = cy + y_delta[i]
                if neighbor_x >= -2 and neighbor_y >= -2:
                    res.append((neighbor_x, neighbor_y, move_num + 1))

            return res
                
        def bfs(root):
            queue = deque([root])
            visited = set([(0, 0)])

            while len(queue) > 0:
                node = queue.popleft()
                node_x, node_y, node_moves = node
                if node_x == x and node_y == y:
                    return node_moves
                    
                for neighbor in get_neighbors(node):
                    nx, ny, nm = neighbor
                    if (nx, ny) in visited:
                        continue

                    queue.append(neighbor)
                    visited.add((nx, ny))

            return -1
            
            
        return bfs((0, 0, 0))
