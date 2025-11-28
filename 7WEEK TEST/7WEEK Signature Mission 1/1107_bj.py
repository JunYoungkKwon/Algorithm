from itertools import permutations

N = input() #이동하려고 하는 채널
M = int(input()) #고장난 버튼의 개수
error_btn = list(map(int, input().split())) #고장난 버튼

channel = 100
btn = [0,1,2,3,4,5,6,7,8,9]

for btn_del in error_btn:
    btn.remove(btn_del)

#수빈이가 지금 보고 있는 채널은 100번

#버튼 누르는게 먼저인데 버튼을 어떻게 누를지 고민

# while True:

    #버튼 누르기
    for com in permutations(btn, len(N)):
        a = int(''.join(map(str, com)))
        if len(str(a)) == len(N):
            abs(a-int(N))

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())  # 고장난 버튼 개수
broken = set(input().split()) if M else set()

# 1. +/-로만 이동하는 경우
answer = abs(N - 100)

# 2. 0 ~ 999999까지 전부 검사
for num in range(1000000):
    num_str = str(num)

    # 누를 때 고장난 버튼이 포함되어 있으면 스킵
    for ch in num_str:
        if ch in broken:
            break
    else:
        # 모든 숫자를 누를 수 있음 → 버튼 누르는 횟수 + 거리 조정
        press_count = len(num_str)
        move_count = abs(num - N)
        answer = min(answer, press_count + move_count)

print(answer)







