# https://leetcode.com/problems/surrounded-regions/
# Runtime: 102 ms -> beats 99.59% of users with Python3

class Solution:
    # Runtime: O(n*m)
    def bfs(self, board: list[list[str]], r: int, c: int) -> None:
        queue = [(r, c)]
        while len(queue) != 0:
            currR, currC = queue.pop(0)
            # Check north neighbour
            if currR - 1 > -1 and self.visited[currR - 1][currC] == False:
                self.visited[currR - 1][currC] = True
                if board[currR - 1][currC] == "O":
                    queue.append((currR - 1, currC))
            # Check south neighbour
            if currR + 1 < self.m and self.visited[currR + 1][currC] == False:
                self.visited[currR + 1][currC] = True
                if board[currR + 1][currC] == "O":
                    queue.append((currR + 1, currC))
            # Check east neighbour
            if currC + 1 < self.n and self.visited[currR][currC + 1] == False:
                self.visited[currR][currC + 1] = True
                if board[currR][currC + 1] == "O":
                    queue.append((currR, currC + 1))
            # Check west neighbour
            if currC - 1 > -1 and self.visited[currR][currC - 1] == False:
                self.visited[currR][currC - 1] = True
                if board[currR][currC - 1] == "O":
                    queue.append((currR, currC - 1))
    # end dfs

    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # The only way a region is not 4-directionally surrounded is if
        # the region has at least one cell on the edge of the grid.
        # Therefore, check all cells on the edges of the board and apply
        # DFS at each to mark the regions as visited. Then, for all
        # cells that were not visited, flip it from "O" to "X"
        self.m = len(board)
        self.n = len(board[0])
        self.visited = [[False for _ in range(self.n)] for _ in range(self.m)]
        if self.m <= 2 or self.n <= 2: # no center ?
            return
        # Left of grid
        for i in range(self.m):
            if self.visited[i][0] == False:
                self.visited[i][0] = True
                if board[i][0] == "O":
                    self.dfs(board, i, 0)
        # Right of grid
        for i in range(self.m):
            if self.visited[i][self.n-1] == False:
                self.visited[i][self.n-1] = True
                if board[i][self.n-1] == "O":
                    self.dfs(board, i, self.n-1)
        # Top of grid
        for i in range(self.n):
            if self.visited[0][i] == False:
                self.visited[0][i] = True
                if board[0][i] == "O":
                    self.dfs(board, 0, i)
        # Bottom of grid
        for i in range(self.n):
            if self.visited[self.m-1][i] == False:
                self.visited[self.m-1][i] = True
                if board[self.m-1][i] == "O":
                    self.dfs(board, self.m-1, i)
        # Flip all cells in center that were not visited
        for r in range(1, self.m - 1):
            for c in range(1, self.n - 1):
                if self.visited[r][c] == False and board[r][c] == "O":
                    board[r][c] = "X"
    # end solve
# end Solution

if __name__ == "__main__":
    sol = Solution()
    board = [
        ["X","X","X","X"],
        ["X","O","O","X"],
        ["X","X","O","X"],
        ["X","O","X","X"]
    ]
    sol.solve(board)
    assert(board == [
        ["X","X","X","X"],
        ["X","X","X","X"],
        ["X","X","X","X"],
        ["X","O","X","X"]
    ])

    board = [["X"]]
    sol.solve(board)
    assert(board == [["X"]])

    board = [
        ["O","X","O","O","O","X"],
        ["O","O","X","X","X","O"],
        ["X","X","X","X","X","O"],
        ["O","O","O","O","X","X"],
        ["X","X","O","O","X","O"],
        ["O","O","X","X","X","X"]
    ]
    sol.solve(board)
    print(board)
