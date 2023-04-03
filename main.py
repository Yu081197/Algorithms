import sys

from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0, 0, 0]  # 가로
dy = [0, 0, -1, 1, 0, 0]  # 세로
dz = [0, 0, 0, 0, -1, 1]  # 높이

while True:
    L, R, C = map(int, input().split())
    if L == 0 and R == 0 and C == 0:
        break
    graph = []
    visit = [[[False] * C for _ in range(R)] for _ in range(L)]
    for _ in range(L):
        graph.append([list.input().strip() for _ in range(R)])
        temp = input()

        q = deque()
        escape = False
