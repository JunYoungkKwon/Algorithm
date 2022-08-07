#row = x col = y
#평소 x -> y / y -> x
import copy
def solution(rows, columns, queries):
    answer = []
    board = [[0] * columns for _ in range(rows)]
    k = 1
    #기본 보드 만들기
    for i in range(rows):
        for j in range(columns):
            board[i][j] = k
            k += 1

    for que in queries:
        min_num = 999999
        chk = copy.deepcopy(board)
        y1, x1, y2, x2 = map(lambda x:x-1, que)
        # print(f'{y1}{x1}{y2}{x2}')
        for s in range(y1, y2+1):
            for e in range(x1, x2 + 1):
                # ->
                if x1 < e < x2 + 1 and s == y1:
                    board[s][e] = chk[s][e - 1]
                    min_num = min(min_num, board[s][e])
                # <-
                if x1 <= e < x2 and s == y2:
                    board[s][e] = chk[s][e + 1]
                    min_num = min(min_num, board[s][e])
                # <i
                if e == x1 and y1 <= s < y2:
                    board[s][e] = chk[s + 1][e]
                    min_num = min(min_num, board[s][e])
                # i>
                if e == x2 and y1 < s < y2 + 1:
                    board[s][e] = chk[s - 1][e]
                    min_num = min(min_num, board[s][e])
        answer.append(min_num)

        # for n in range(rows):
        #     print(*board[n])

    return answer

print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
