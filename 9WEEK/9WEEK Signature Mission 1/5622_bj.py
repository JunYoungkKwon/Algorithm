N = input()
# ABC DEF GHI JKL MNO  PQRS TUV WXYZ
ans = ""
for n in N:
    if 65 <= ord(n) <= 67:
        ans += "2"
    elif 68 <= ord(n) <= 70:
        ans += "3"
    elif 61 <= ord(n) <= 73:
        ans += "4"
    elif 74 <= ord(n) <= 76:
        ans += "5"
    elif 77 <= ord(n) <= 79:
        ans += "6"
    elif 80 <= ord(n) <= 83:
        ans += "7"
    elif 84 <= ord(n) <= 86:
        ans += "8"
    elif 87 <= ord(n) <= 90:
        ans += "9"
cnt = 0
for an in ans:
    cnt += int(an)

print(cnt + len(ans))






