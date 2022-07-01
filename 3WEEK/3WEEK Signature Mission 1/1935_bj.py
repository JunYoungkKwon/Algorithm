N = int(input())
li = list(input())
nums = [int(input()) for _ in range(N)]
ans = []
for i in li:
    if i.isalpha():
        ans.append(nums[ord(i) - ord('A')])

    else:
        a = ans.pop()
        b = ans.pop()
        if i == '+':
            ans.append(b + a)
        elif i == '-':
            ans.append(b - a)
        elif i == '*':
            ans.append(b * a)
        elif i == '/':
            ans.append(b / a)
print(f'{ans[0]:0.2f}')