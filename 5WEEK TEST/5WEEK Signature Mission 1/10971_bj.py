# 어느 한 도시에서 출발해 N개의 도시를 모두 거쳐 다시 원래의 도시로 돌아옴
# 단, 한 번 갔던 도시로는 다시 갈 수 없다.
# 가장 적은 비용을 들이는 여행 계획
# TSP문제


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
chk = [False] * (N+1)


#최소값 비교라 min_sum 최소값을 지정해줘야 할듯
def backtracking(sum, depth, first_num, last_num):
    global min_sum

    if depth == 5:
        min_sum = min(min_sum, sum)

    #체크I의 위치를 바꿔야 할듯 이러면 백트래킹으로 I가 안변함
    for i in range(1, N+1):
        chk[i] = True
        for j in range(1, N+1):
            if board[i][j] != 0:
                #첫 출발
                if not chk[j] and depth == 0:
                    chk[j] = True
                    backtracking(sum + board[i][j],depth+1, i, last_num)
                    chk[j] = False
                #다음 출발


backtracking(0, 0, 0, 0)
print(min_sum)