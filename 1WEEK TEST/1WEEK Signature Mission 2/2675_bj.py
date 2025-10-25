T = int(input())
for _ in range(T):
    R, S = map(str, input().split())
    for r in S:
        print(r*int(R), end="")
    print()




