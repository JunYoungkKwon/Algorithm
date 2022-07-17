str = input()
ans = ""
ans += str[0]
for i in range (1, len(str)):
    if str[i] == '-':
        ans += str[i+1]
print(ans)