import sys
# input = sys.stdin.readline

# 함수 R은 배열에 있는 수의 순서를 뒤집는 함수이고
# D는 첫 번째 수를 버리는 함수이다
# 배열이 비어있는데 D를 사용한 경우에는 에러가 발생한다


T = int(input())

for _ in range(T):
    p = input().rstrip() #함수
    n = int(input()) #배열 갯수
    s = input()
    if n == 0:
        arr = ""
    else:
        arr = list(map(int, s.strip('[]').split(',')))
    for i in p:
        if i == 'R':
            if arr:
                arr.reverse()

        else:
            if arr:
                arr.pop(0)
            else:
                print("error")
    print(arr)
