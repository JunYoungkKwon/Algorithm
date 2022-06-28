# 딕셔너리 문제
# max는 딕셔너리 중에서 최대 값이 2개여도 가장 앞에 있는 하나만 출력 함.
# 그래서 정렬을 하고 max 값을 구해야 오류가 안남.
N = int(input())
book = {}
for _ in range(N):
    title = input()
    if title in book:
        book[title] += 1
    else:
        book[title] = 1
book = dict(sorted(book.items()))
max_num = max(book, key=book.get)
print(max_num)

