def solution(v):
    if v[0][0] == v[1][0]:
        x = v[2][0]
    else:
        if v[0][0] == v[2][0]:
            x = v[1][0]
        if v[1][0] == v[2][0]:
            x = v[0][0]

    if v[0][1] == v[1][1]:
        y = v[2][1]
    else:
        if v[0][1] == v[2][1]:
            y = v[1][1]
        if v[1][1] == v[2][1]:
            y = v[0][1]


    answer = [x, y]


    return answer
print(solution([[1, 4], [3, 4], [3, 10]]))
#[[1, 4], [3, 4], [3, 10]] 결과 [1, 10]