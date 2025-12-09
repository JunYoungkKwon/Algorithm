progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]
def solution(progresses, speeds):
    days = []
    for p, s in zip(progresses, speeds):
        # 남은 작업일 계산 (100 - p) / s 올림
        remain = (100 - p + s - 1) // s
        days.append(remain)

    answer = []
    current = days[0]
    count = 1

    for d in days[1:]:
        if d <= current:
            count += 1
        else:
            answer.append(count)
            current = d
            count = 1

    answer.append(count)
    print(answer
          )
    return answer

solution(progresses, speeds)