import sys
input = sys.stdin.readline

enter_name = {}

for i in range(int(input())):
    name, log = input().rstrip().split()
    if log == "enter":
        enter_name[name] = 1

    else:
        enter_name[name] = 0

ans = [key for key, v in enter_name.items() if v == 1]

# print(ans)
#현재 회사에 있는 사람의 이름을 사전 순의 역순으로 한 줄에 한 명씩 출력
for i in sorted(ans, reverse=True):
    print(i)