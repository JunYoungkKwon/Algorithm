# 랭킹 리스트에 올라 갈 수 있는 점수의 개수 P
# 리스트에 있는 점수 N
# 첫째 줄에 N, 태수의 새로운 점수, P
N, new_record, P = map(int, input().split())
ans = 0
if N == 0:
    print(1)
else:
    record = sorted(list(map(int, input().split())))
    for score in range(N):
        if  N == P and record[0] >= new_record:
            print(-1)
            exit()
        else:
            if record[score] > new_record:
                ans += 1

    print(ans+1)