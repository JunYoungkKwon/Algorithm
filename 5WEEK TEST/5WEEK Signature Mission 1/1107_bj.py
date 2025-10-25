from itertools import product

N = int(input())  # 목표 채널
M = int(input())  # 고장난 버튼 개수

broken = set(map(int, input().split())) if M else set()
buttons = {0,1,2,3,4,5,6,7,8,9} - broken

# 1. +, - 로만 이동하는 경우
ans = abs(N - 100)

# 2. 숫자 버튼으로 직접 누르는 경우 (1~6자리까지 시도)
for length in range(1, 7):
    for nums in product(buttons, repeat=length):  # 중복순열
        num = int(''.join(map(str, nums)))
        ans = min(ans, abs(N - num) + len(str(num)))

print(ans)
