# 문자열 인덱스로 처리하려 했는데 생각하고 보니 0시 0분부터 주어지면 에러가 난다..
# ㅋㅋㅋ...방심하지말자 ㅠ
H, M = map(int, input().split())
timer = int(input())

H += timer // 60
M += timer % 60

if M >= 60:
    H += 1
    M -= 60
if H >= 24:
    H -= 24

print(H,M)