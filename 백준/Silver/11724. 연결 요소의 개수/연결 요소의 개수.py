import sys

sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

N, M = map(int, input().split())
adj = [[0] * N for _ in range(N)]
for _ in range(M):
    u, v = map(lambda x: x - 1, map(int, input().split()))
    adj[u][v] = adj[v][u] = 1

chk = [False] * N
ans = 0


def dfs(now):
    for nxt in range(N):
        if adj[now][nxt] and not chk[nxt]:
            chk[nxt] = True
            dfs(nxt)


for i in range(N):
    if not chk[i]:
        chk[i] = True
        ans += 1
        dfs(i)

print(ans)
