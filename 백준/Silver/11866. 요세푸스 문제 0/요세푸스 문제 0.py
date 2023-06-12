from collections import deque
import sys

n, k = map(int, input().split())
d = deque([i for i in range(1, n+1)]) # 1부터 n까지의 원소 삽입
result = []

for i in range(n): # n개의 원소 꺼내기
    for i in  range(k - 1): # k-1번 "왼쪽으로 돌리기" 수행
        x = d.popleft()
        d.append(x)
    x = d.popleft()
    result.append(x)
    
print('<', end='')
for i in range(len(result)):
    if i < len(result) - 1:
        print(result[i], end=', ')
    else:
        print(result[i], end='')
print('>')