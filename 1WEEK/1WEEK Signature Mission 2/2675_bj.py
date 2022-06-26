N = int(input())
for _ in range(N):
    x, y = map(str, input().split())
    string = ""
    for i in range(len(y)):
        string += y[i] * int(x)
    print(string)