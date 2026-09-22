class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        visited = set()
        n, m = len(board), len(board[0])

        def dfs(i, j):
            curr_set = set()
            stack = [(i, j)]
            legal = True

            while stack:
                i, j = stack.pop()

                if i < 0 or i >= n or j < 0 or j >= m:
                    continue

                if board[i][j] == "X" or (i, j) in curr_set:
                    continue

                curr_set.add((i, j))

                if i == 0 or i == n - 1 or j == 0 or j == m - 1:
                    legal = False

                stack.append((i - 1, j))
                stack.append((i + 1, j))
                stack.append((i, j - 1))
                stack.append((i, j + 1))

            return legal, curr_set

        for i in range(1, n - 1):
            for j in range(1, m - 1):

                if board[i][j] != "O" or (i, j) in visited:
                    continue

                legal, curr_set = dfs(i, j)

                if legal:
                    for x, y in curr_set:
                        board[x][y] = "X"
                else:
                    visited.update(curr_set)