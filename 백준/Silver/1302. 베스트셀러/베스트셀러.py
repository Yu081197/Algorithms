import sys
n = int(input())

books = {}

for _ in range(n):
    book = input()
    if book not in books:  # books에 book이 들어있지 않다면
        books[book] = 1  # books에 해당 book을 추가하고 값은 1로 함
    else:
        books[book] += 1  # 들어있다면 해당 값을 1 늘려줌 즉, 들어있는 만큼 숫자를 늘리는 것

target = max(books.values())  # target은 books에 가장 많이 들어있는 값 즉 book의 값
arr = []

for book, number in books.items():  # book, number에 대해서 books의 개수만큼 반복한다.
    if number == target: # number가 가장 많이 들어있는 값이라면
        arr.append(book) # arr에다가 해당 book을 추가 ex) ['top']

print(sorted(arr)[0]) # 가장 많은 순으로 정렬하고 0번째를 출력한다.
