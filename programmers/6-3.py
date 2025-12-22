def solution(number, k):
    stk = []
    for n in number:
        while stk and k > 0 and stk[-1] < n:
            stk.pop()
            k -= 1
        stk.append(n)

    if k > 0:
        stk = stk[:-k]
    return "".join(stk)        