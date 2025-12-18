from itertools import permutations


def solution(k, dungeons):
    max_ans = 0
    for per in permutations(dungeons, len(dungeons)):
        answer = 0
        n = k
        for p, d in per:
            if n >= p:
                n -= d
                answer += 1
            else:
                break
        max_ans = max(max_ans, answer)

    return max_ans
