#
# stk_left = []
# stk_right = []
#
# string = input().strip()
# ans = 0
# left = 0
# right = 0
# for i in string:
#     if i == '(':
#         stk_left.append(i)
#
#     elif i == '[':
#         stk_right.append(i)
#
#     elif i == ')':
#         if stk_left:
#             if stk_left.pop() == '(':
#                 if stk_left:
#                     left += 2
#                 else:
#                     if not stk_left and not stk_right:
#                         ans += (left + right) * 2
#                         left = 0
#                         right = 0
#     elif i == ']':
#         if stk_right:
#             if stk_right.pop() == '[':
#                 if stk_right:
#                     right += 3
#                 else:
#                     if not stk_left and not stk_right:
#                         ans += (left + right) * 3
#                         left = 0
#                         right = 0
#
#
# #for문을 다돌고 스택에 남아있으면
# if stk_left or stk_right:
#     print(0)
# else:
#     print(ans)
string = input().strip()
stk = []
ans = 0
temp = 1

for i in range(len(string)):
    ch = string[i]

    if ch == '(':
        stk.append(ch)
        temp *= 2  # 괄호가 열릴 때 2배
    elif ch == '[':
        stk.append(ch)
        temp *= 3  # 대괄호가 열릴 때 3배
    elif ch == ')':
        # 올바른 괄호가 아닌 경우
        if not stk or stk[-1] != '(':
            ans = 0
            break
        # 직전 문자가 '('라면 즉시 더함
        if string[i - 1] == '(':
            ans += temp
        stk.pop()
        temp //= 2  # 닫을 때 다시 나눔
    elif ch == ']':
        if not stk or stk[-1] != '[':
            ans = 0
            break
        if string[i - 1] == '[':
            ans += temp
        stk.pop()
        temp //= 3

# 스택이 비어있지 않으면 잘못된 괄호
if stk:
    print(0)
else:
    print(ans)

