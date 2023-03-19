# 미로 탐색
from sys import stdin
from collections import deque


def bfs():
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    while queue:
        r, c = queue.popleft()

        if r == n - 1 and c == m - 1:
            print(visited[r][c])
            break

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                continue

            if visited[nr][nc] == 0 and maze[nr][nc] == 1:  # 아직 방문하지 않았고, 이동할 수 있다면
                visited[nr][nc] = visited[r][c] + 1
                queue.append((nr, nc))


n, m = map(int, stdin.readline().split())
maze = [list(map(int, stdin.readline().strip())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

# 시작 위치
queue = deque([(0, 0)])
visited[0][0] = 1
bfs()
