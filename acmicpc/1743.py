import sys
from collections import deque

sys.setrecursionlimit(10 ** 4)

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

N, M, K = map(int, sys.stdin.readline().split())
graph = [[0] * M for _ in range(N)]

for _ in range(K):
    y, x = map(int, input().split())
    graph[y - 1][x - 1] = '#'


visit = [[False] * M for _ in range(N)]
sz = 0
ans = 0


def is_valid_coord(y, x):
    return 0 <= y < N and 0 <= x < M


def dfs(y, x):
    global ans, sz

    visit[y][x] = True
    sz += 1
    ans = max(ans, sz)

    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if is_valid_coord(ny, nx) and not visit[ny][nx] and graph[ny][nx] == '#':
            dfs(ny, nx)


for i in range(N):
    for j in range(M):
        if not visit[i][j] and graph[i][j] == '#':
            sz = 0
            dfs(i, j)

print(ans)
