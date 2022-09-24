def getMyDivisor(n):
    divisorsList = []

    for i in range(1, int(n ** (1 / 2)) + 1):
        if (n % i == 0):
            divisorsList.append(i)
            if ((i ** 2) != n):
                divisorsList.append(n // i)

    divisorsList.sort()

    return divisorsList

def solution(brown, yellow):
    answer = []
    li = getMyDivisor(brown+yellow)
    while li:
        le = li[0]
        ri = li[-1]
        print(f"{le} {ri}")
        del li[0]
        if li:
            del li[-1]
        if (le - 2) * (ri - 2) >= yellow:
            answer.append(le)
            answer.append(ri)
            break
    answer.reverse()

    return answer

print(solution(24, 24))
# 갈색 격자의 수 brown은 8 이상 5,000 이하인 자연수입니다.
# 노란색 격자의 수 yellow는 1 이상 2,000,000 이하인 자연수입니다.
# 카펫의 가로 길이는 세로 길이와 같거나, 세로 길이보다 깁니다.
# 10	2	[4, 3]
# 8	1	[3, 3]
# 24	24	[8, 6]