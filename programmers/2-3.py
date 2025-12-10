import math
s = "(()("
def solution(s):
    stk = []
    math.floor(8/2)
    answer = True
    for i in s:
        if i == "(":
            stk.append(i)
        else:
            if stk:
                stk.pop()
            else:
                return False
    if stk:
        return False
    else:
        return True

print(solution(s))