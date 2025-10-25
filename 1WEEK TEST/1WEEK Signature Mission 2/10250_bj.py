T = int(input())

6 12 75 512번

8 / 6 몫
72 / 6
for i in range(T):
    H, W, N = map(int, input().split())

    floor = N % H #나머지
    room_num = (N // H) + 1 #몫


