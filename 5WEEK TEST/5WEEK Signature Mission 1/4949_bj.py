while True:
    N = input()
    if N == '.':
        break

    stk = []
    balanced = True

    for a in N:
        if a in '([':
            stk.append(a)
        elif a == ')':
            if stk and stk[-1] == '(':
                stk.pop()
            else:
                balanced = False
                break
        elif a == ']':
            if stk and stk[-1] == '[':
                stk.pop()
            else:
                balanced = False
                break
        # 나머지 문자는 무시

    if balanced and not stk:
        print('yes')
    else:
        print('no')
