class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        nrows = len(grid)
        ncols = len(grid[0])

        def locate_treasures():
            res = []
            for r in range(nrows):
                for c in range(ncols):
                    if grid[r][c] == 0:
                        res.append((r, c))
            return res

        def find_neighbors(node):
            row, col = node
            delta_row = [-1, 0, 1, 0]
            delta_col = [0, 1, 0, -1]
            res = []
            for i in range(len(delta_row)):
                neighbor_row = row + delta_row[i]
                neighbor_col = col + delta_col[i]

                if 0 <= neighbor_row < nrows and 0 <= neighbor_col < ncols:
                    coord_val = grid[neighbor_row][neighbor_col]
                    if coord_val != -1 and grid[row][col] + 1 < grid[neighbor_row][neighbor_col]:
                        res.append((neighbor_row, neighbor_col))

            return res

        def bfs(treasures):
            queue = deque(treasures)
            while len(queue) > 0:
                node = queue.popleft()
                cr, cc = node
                for neighbor in find_neighbors(node):
                    nr, nc = neighbor
                    grid[nr][nc] = grid[cr][cc] + 1
                    queue.append(neighbor)

        treasures = locate_treasures()
        bfs(treasures)