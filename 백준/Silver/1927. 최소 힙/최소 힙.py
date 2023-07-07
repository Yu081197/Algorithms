import heapq
import sys
input = sys.stdin.readline

n = int(input())
heap = []
result = []
for i in range(n):
    x = int(input())
    if x == 0: # x 값이 0이라면
        if heap: # heap에 값이 있다면
            result.append(heapq.heappop(heap)) # result에 있는 값을 heappop함
        else: # heap에 값이 없다면
            result.append(0) # result에 0 추가
    else: # x 값이 0이 아니라면
        heapq.heappush(heap, x) # heap에 x값 추가

for x in result:
    print(x)