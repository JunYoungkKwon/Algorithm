def solution(lottos, win_nums):
    answer = []
    cnt = 0
    zero_cnt = 0
    for win_num in win_nums:
        for lotto_num in lottos:
            if win_num == lotto_num:
                cnt += 1
    for lotto_num in lottos:
        if lotto_num == 0:
            zero_cnt += 1
    ans = cnt + zero_cnt
    #최고
    if ans == 6:
        answer.append(1)
    elif ans == 5:
        answer.append(2)
    elif ans == 4:
        answer.append(3)
    elif ans == 3:
        answer.append(4)
    elif ans == 2:
        answer.append(5)
    else:
        answer.append(6)
    #최저
    if cnt == 6:
        answer.append(1)
    elif cnt == 5:
        answer.append(2)
    elif cnt == 4:
        answer.append(3)
    elif cnt == 3:
        answer.append(4)
    elif cnt == 2:
        answer.append(5)
    else:
        answer.append(6)
    return answer

