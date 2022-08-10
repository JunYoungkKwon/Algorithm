#오류 문자 대문자 출력해서 틀림 ㅠ 정신 차리고 풀자
total = int(input())
ans = 0
for i in range(int(input())):
    a, b = map(int, input().split())
    ans += a*b
    # print(ans)

if ans == total:
    print("Yes")
else:
    print("No")