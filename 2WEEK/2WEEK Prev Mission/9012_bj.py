for _ in range (int(input())):
    stk = []
    is_tf = True
    for ch in (input()):
        if ch == '(':
            stk.append(ch)
        else:
            if stk:
                stk.pop()
            else:
                is_tf = False
                break
    if stk:
        is_tf = False
    print( 'YES' if is_tf else 'NO')
