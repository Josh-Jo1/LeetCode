# https://leetcode.com/problems/number-of-islands/
# Runtime: 208 ms -> beats 99.27% of users with Python3

class Solution:
    # Runtime: O(n*m)
    def numIslands(self, grid: list[list[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        count = 0
        for r in range(0, m):
            for c in range(0, n):
                if visited[r][c] or grid[r][c] == "0":
                    continue
                # Discovered new island
                visited[r][c] = True
                queue = [(r, c)]
                while len(queue) != 0:
                    currR, currC = queue.pop(0)
                    # Check north neighbour
                    if currR - 1 > -1 and not visited[currR - 1][currC]:
                        visited[currR - 1][currC] = True
                        if grid[currR - 1][currC] == "1":
                            queue.append((currR - 1, currC))
                    # Check south neighbour
                    if currR + 1 < m and not visited[currR + 1][currC]:
                        visited[currR + 1][currC] = True
                        if grid[currR + 1][currC] == "1":
                            queue.append((currR + 1, currC))
                    # Check east neighbour
                    if currC + 1 < n and not visited[currR][currC + 1]:
                        visited[currR][currC + 1] = True
                        if grid[currR][currC + 1] == "1":
                            queue.append((currR, currC + 1))
                    # Check west neighbour
                    if currC - 1 > -1 and not visited[currR][currC - 1]:
                        visited[currR][currC - 1] = True
                        if grid[currR][currC - 1] == "1":
                            queue.append((currR, currC - 1))
                count += 1
        return count
    # end numIslands
# end Solution

if __name__ == "__main__":
    sol = Solution()
    assert sol.numIslands([
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
        ]) == 1
    assert sol.numIslands([
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
        ]) == 3
    print(sol.numIslands([
        ["1","1","1"],
        ["0","1","0"],
        ["1","1","1"]
        ]))
