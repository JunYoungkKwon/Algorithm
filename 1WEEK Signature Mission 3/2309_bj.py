from itertools import combinations
A = [int(input()) for _ in range(9)]
for com in combinations(A, 7):

    if sum(com) == 100:
        a = list(com)
        a.sort()
        for i in a:
            print(i)
        #3040 문제는 답이 유일하기 때문에 문제 없지만 2039는 여러 개 일 경우가 있어서 경우 하나를 출력하고서 exit 해야 오류가 안남
        exit()
