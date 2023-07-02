
document = input()
word = input()

index = 0
result = 0
while len(document) - index >= len(word):
    if document[index:index + len(word)] == word:  # 지금 인덱스의 단어가 찾고자 하는 단어인 경우
        result += 1
        index += len(word)  # word의 길이만큼 인덱스를 늘려준다
    else:
        index += 1

print(result)
