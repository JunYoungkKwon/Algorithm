def solution(balance, countries):
    answer = -1
    n = len(countries)
    visited = [False] * n

    def dfs(cnt, money):
        nonlocal answer
        answer = max(answer, cnt)

        for i in range(n):
            if countries[i][1] <= money and not visited[i]:
                visited[i] = True
                dfs(cnt+1, money-countries[i][0])
                visited[i] = False



    dfs(0, balance)

    return answer

print(solution(500, [[250,250],[300,400],[120,450],[70,150]]))