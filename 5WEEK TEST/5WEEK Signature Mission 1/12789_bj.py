# 승환이가 무사히 간식을 받을 수 있으면 "Nice"
# 를 출력하고 그렇지 않다면 "Sad"(따옴표는 제외)를 출력한다.

N = int(input())
li = list(map(int, input().split()))
stack = []
turn = 1

for x in li:
    stack.append(x)
    # stack top이 다음 순번과 맞으면 계속 꺼냄
    while stack and stack[-1] == turn:
        stack.pop()
        turn += 1

if turn == N + 1:
    print("Nice")
else:
    print("Sad")






