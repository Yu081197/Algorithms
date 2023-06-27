import heapq
import sys


input = sys.stdin.readline

t = int(input())


def show_result():
    print(len(result))  # 출력할 총 원소의 개수
    for i in range(len(result)):
        print(result[i], end=' ')
        if (i + 1) % 10 == 0:  # 10개 단위로 줄바꿈
            print()
    print()


for _ in range(t):
    m = int(input())
    data = []
    for i in range(m // 10+1):
        data.extend(list(map(int, input().split())))  # 수열 입력
    left = []  # 왼쪽 최대 힙 (원소를 삽입/)
    right = []  # 오른쪽 최소 힙
    median = data[0]  # 중앙값
    result = [median]  # 결과 배열
    for i in range(1, m):  # 수열의 원소를 하나씩 확인하며
        if data[i] <= median:  # 중앙값보다 작다면
            heapq.heappush(left, -data[i])  # left에 삽입
        else:
            heapq.heappush(right, data[i])
        if i % 2 == 0:  # 2개 확인할때마다
            if len(left) > len(right):  # 왼쪽의 길이가 더 크다면
                heapq.heappush(right, median)  # right으로 중앙값을 옮긴다
                median = -heapq.heappop(left)  # 중앙값은 left에서 최대 값을 가져온다
            elif len(left) < len(right):  # 오른쪽의 길이가 더 크다면
                heapq.heappush(left, -median)  # left으로 중앙값을 옮긴다
                median = heapq.heappop(right)  # 중앙값은 right에서 최대 값을 가져온다
            result.append(median)
    show_result()
