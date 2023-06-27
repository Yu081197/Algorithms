import heapq
import sys

input = sys.stdin.readline

n = int(input())  # 강의 개수 입력받기
lectures = []
for i in range(n):
    id, start, end = map(int, input().split())  # 강의번호, 시작시간, 종료시간 입력
    heapq.heappush(lectures, (start, end))  # 시작시간 종료시간을 기준으로 힙에 삽입

heap = []  # 배정된 강의실
end = heapq.heappop(lectures)[1]  # 첫 번째 강의가 끝나는 시간을 우선순위 큐에 삽입
heapq.heappush(heap, end)
answer = 1  # 필요한 강의실 개수

for i in range(n - 1):
    new_start, new_end = heapq.heappop(lectures)  # 강의 목록에서 [새 강의] 꺼내기
    end = heapq.heappop(heap)  # [기존 강의] 중에서 가장 일찍 끝나는 강의 꺼내기

    if new_start < end:  # 강의시간이 만약 겹친다면?
        heapq.heappush(heap, end)  # 기존 강의실은 유지
        heapq.heappush(heap, new_end)  # 새로운 강의실 추가
        answer += 1
    else:  # 겹치지 않는다면
        heapq.heappush(heap, new_end)  # 기존 강의실에 배정

print(answer)
