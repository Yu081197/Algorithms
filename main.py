from collections import deque

# 나이트의 이동 방향
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]


def bfs(x, y, end_x, end_y, chess_size):
    # 방문 여부를 체크하는 2차원 리스트
    visited = [[False] * chess_size for _ in range(chess_size)]
    # 출발지점을 큐에 추가
    q = deque([(x, y, 0)])
    visited[x][y] = True

    while q:
        cur_x, cur_y, count = q.popleft()

        if cur_x == end_x and cur_y == end_y:
            # 목적지에 도착했을 때, 이동 횟수를 리턴
            return count

        # 나이트가 이동할 수 있는 8가지 방향에 대해 탐색
        for i in range(8):
            nx, ny = cur_x + dx[i], cur_y + dy[i]
            # 체스판을 벗어나지 않는 범위에서 탐색하며, 방문하지 않은 지점이라면 큐에 추가
            if 0 <= nx < chess_size and 0 <= ny < chess_size and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny, count+1))

    return 0  # 목적지에 도달하지 못한 경우 0을 리턴


# 입력 예시
t = int(input())
for _ in range(t):
    chess_size = int(input())
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())

    # bfs 탐색 실행
    answer = bfs(start_x, start_y, end_x, end_y, chess_size)
    print(answer)
