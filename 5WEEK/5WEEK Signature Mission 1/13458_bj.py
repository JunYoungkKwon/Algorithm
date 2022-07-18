# 문제 이해를 잘못했음 총감독이 무조건 있어야 함..
N = int(input())
li = list(map(int, input().split()))
A, B = map(int, input().split())
ans = 0
for stu in li:
        stu -= A
        ans += 1
        if stu > 0:
            if stu % B:
                ans += (stu // B) + 1
            else:
                ans += (stu // B) + 0

print(ans)

