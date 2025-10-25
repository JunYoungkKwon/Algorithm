S = input()
dic ="abcdefghijklmnopqrstuvwxyz"
for d in dic:
    if d in S:
        print(S.find(d), end=" ")
    else:
        print(-1, end=" ")