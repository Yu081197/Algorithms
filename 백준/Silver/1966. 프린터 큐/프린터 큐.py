tc = int(input())
for _ in range(tc):
    n, m = list(map(int, input().split(' ')))
    queue = list(map(int, input().split(' '))) # [2, 1, 4, 3]
    queue = [(i, idx) for idx, i in enumerate(queue)] # enumerate는 인덱스와 함께 튜플로 저장하는 함수 => [(2, 0),(1, 1),(4, 2),(3, 3)]
    count = 0
    
    while  True:
        if queue[0][0] == max(queue, key=lambda x: x[0])[0]:
            count += 1
            if queue[0][1] == m:
                print(count)
                break
            else:
                queue.pop(0)
        else:
            queue.append(queue.pop(0))