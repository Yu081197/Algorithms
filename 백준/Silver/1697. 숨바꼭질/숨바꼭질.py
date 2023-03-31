from collections import deque

n, k = map(int, input().split())


def bfs():
    queue = deque()
    queue.append(n)
    while queue:
        x = queue.popleft()  # x는 큐 왼쪽에서 빼낸 값
        if x == k:  # 빼낸 값이 k와 같다면
            print(dist[x])  # x를 빼낸다
            break
        for nx in (x - 1, x + 1, 2 * x):  # x의 방향 설정
            if 0 <= nx <= MAX and not dist[nx]:  # 방문체크
                dist[nx] = dist[x] + 1
                queue.append(nx)


MAX = 10 ** 5
dist = [0] * (MAX + 1)

bfs()
