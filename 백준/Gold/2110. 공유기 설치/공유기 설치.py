import sys
input = sys.stdin.readline

n, c = map(int, input().split())


array = []
for i in range(n):
    array.append(int(input()))

array.sort()

start = 1 # 최소 거리
end = array[-1] - array[0] # 최대 거리
answer = 0


def binary_search(array, start, end):
    while start <= end:
        mid = (start + end) // 2 # 가운대 수
        current = array[0] # 현재 탐색하는 수
        count = 1 # count 최소 1

        for i in range(1, len(array)): # 1부터 arr 길이만큼 반복
            if array[i] >= current + mid: # 현재 집의 좌표가 이전에 설치한 공유기와의 거리 이상이라면 공유기를 설치함.
                count += 1
                current = array[i]

        if count >= c: # c개 이상의 공유기를 설치 할 수 있는 경우
            global answer
            start = mid + 1 # gap을 늘려서 더 큰 거리를 탐색하기 위해
            answer = mid # 현재까지의 최대 거리를 갱신
        else: # c개 이상의 공유기를 설치 할 수 없는 경우
            end = mid - 1 # gap을 줄여서 더 작은 거리를 탐색.




binary_search(array, start, end)
print(answer)