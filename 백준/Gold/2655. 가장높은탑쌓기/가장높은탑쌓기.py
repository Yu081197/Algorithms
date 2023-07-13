
import sys


input = sys.stdin.readline

n = int(input())
arr = []
dp = [0] * (n + 1)

arr.append((0,0,0,0))

for i in range(1, n + 1):
    area, height, weight = map(int, input().split())
    arr.append((i, area, height, weight))

arr.sort(key=lambda data: data[3])
for i in range(1, n + 1):
    for j in range(0, i):
        if arr[i][1] > arr[j][1]: # 현재 인덱스 i에서 이전 인덱스 j까지의 부분 문자열 중, 너비가 증가하는 경우에만 부분 문자열의 길이를 업데이트합니다. dp[i]에는 현재 인덱스까지의 최대 부분 문자열의 길이가 저장됩니다.
            dp[i] = max(dp[i],dp[j] + arr[i][2])

max_value = max(dp)
index = n
result = []

while index != 0:
    if max_value == dp[index]:
        result.append(arr[index][0])
        max_value -= arr[index][2]
    index -= 1

result.reverse()
print(len(result))
[print(i) for i in result]