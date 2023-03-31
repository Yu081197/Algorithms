import sys
from collections import deque

input = sys.stdin.readline


def bfs(si, sj, h):  # 시작부분
    q = deque()
    q.append((si, sj))  # 큐에 초기배열 삽입
    visit[si][sj] = 1  # 방문표시

    while q:  # 큐가 진행하는 동안
        ci, cj = q. popleft()  # 현재 큐
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):  # 네 방향으로
            ni, nj = ci + di, cj + dj  # 움직인다
            if 0 <= ni < N and 0 <= nj < N and visit[ni][nj] == 0 and arr[ni][nj] > h:
                q.append((ni, nj))
                visit[ni][nj] = 1


def solve(h):  # h(높이)에 대해 잠기지 않은 영역 개수 리턴
    cnt = 0
    for i in range(N):
        for j in range(N):
            if visit[i][j] == 0 and arr[i][j] > h:  # 만약 탐색하는 지점이 방문하지 않았거나, h보다 높다면
                bfs(i, j, h)  # bfs 실행
                cnt += 1
    return cnt


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = 0

for h in range(100):  # 높이가 0부터 최대 99까지 물 높이 지정
    visit = [[0] * N for _ in range(N)]  # N * N 만큼 0이 들어간 배열 만듦
    ans = max(ans, solve(h))  # 최대값


print(ans)
