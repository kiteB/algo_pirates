# 아기 상어
from sys import stdin
from collections import deque


def bfs():
    dr = [-1, -1, -1, 0, 0, 1, 1, 1]
    dc = [-1, 0, 1, -1, 1, -1, 0, 1]

    while queue:
        r, c = queue.popleft()

        for d in range(8):
            nr = r + dr[d]
            nc = c + dc[d]

            if (0 <= nr < n and 0 <= nc < m) and visited[nr][nc] == 0:  # 범위를 벗어나지 않고 방문하지 않았다면
                visited[nr][nc] = visited[r][c] + 1
                queue.append((nr, nc))


n, m = map(int, stdin.readline().split())
queue = deque()
visited = []

for i in range(n):
    sharks = list(map(int, stdin.readline().split()))
    for j in range(m):
        if sharks[j] == 1:
            queue.append((i, j))
    visited.append(sharks)

bfs()

distance = 0
for i in range(n):
    for j in range(m):
        distance = max(distance, visited[i][j])

print(distance - 1)  # 시작 값은 제외해야 한다
