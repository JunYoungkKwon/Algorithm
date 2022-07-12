# -50 ~ 50까지 범위 인데 -값이 들어가면 어차피 1이고 20 초과 부터는 20,20,20으로 계산하기만 20까지만 3차원 배열 생성
arr = [[[0] * 21 for _ in range(21)] for _ in range(21)]

for a in range(21):
    for b in range(21):
        for c in range(21):
            if a <= 0 or b <= 0 or c <= 0:
                arr[a][b][c] = 1
def w(a, b, c):
    if arr[a][b][c] == 0:
        if a < b and b < c:
            arr[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        else:
            arr[a][b][c] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)

    return arr[a][b][c]

while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    elif a <= 0 or b <= 0 or c <= 0:
        print(f'w({a}, {b}, {c}) = {1}')
    elif a > 20 or b > 20 or c > 20:
        print(f'w({a}, {b}, {c}) = {w(20, 20, 20)}')
    else:
        print(f'w({a}, {b}, {c}) = {w(a, b, c)}')