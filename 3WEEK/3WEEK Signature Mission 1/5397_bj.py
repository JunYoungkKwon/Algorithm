# 마지막을 elif .isalnum() 로 체크하지 않고 else문으로 모든 문자열을 처리하면  and문 때문에 조건을 충족하지 않는 <, > 가 등장함
# 그래서 무조건 알파벳인지 체크 해주는 구문을 추가 해줘야 오류가 안남
# 이 문제도 스택인 것은 눈치 챘지만 구현력이 너무 딸렸음 좀 더 구현력에 집중 해야 될 듯
for _ in range(int(input())):
    stk1= []
    stk2= []
    for i in input():
        if i == "<" and stk1:
            stk2.append(stk1.pop())
        elif i == ">" and stk2:
            stk1.append(stk2.pop())
        elif i == "-" and stk1:
            stk1.pop()
        elif i.isalnum():
            stk1.append(i)

    print("".join(stk1)+"".join(reversed(stk2)))
