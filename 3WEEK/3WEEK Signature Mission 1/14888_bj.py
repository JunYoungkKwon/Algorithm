import sys

input = sys.stdin.readline
N = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))
cnt = 1
li = []

def bfs(plus, minus ,mul, div, cnt, res):
    if cnt == N:
        return li.append(res)
    if plus:
        bfs(plus-1, minus, mul, div, cnt +1, res + num[cnt])
    if minus:
        bfs(plus, minus-1, mul, div, cnt +1, res - num[cnt])
    if mul:
        bfs(plus, minus , mul-1, div, cnt +1, res * num[cnt])
    if div:
        bfs(plus, minus , mul, div-1, cnt +1, int(res / num[cnt]))

bfs(op[0], op[1], op[2], op[3], cnt, num[0])

print(max(li))
print(min(li))

