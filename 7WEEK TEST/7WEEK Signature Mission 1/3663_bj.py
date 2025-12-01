N = int(input())
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
reverse_alpha = "ZYXWVUTSRQPONMLKJIHGFEDCBA"

for _ in range(N):
    ans = 0
    name = input().rstrip()
    for na in name:
        cnt = reverse_alpha.index(na) + 1
        ans += min(abs(ord('A') - ord(na)), cnt)


    print(ans)
