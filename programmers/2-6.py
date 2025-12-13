def solution(prices):
    n = len(prices)
    answer = [0] * n
    stack = []  # 인덱스를 저장하는 스택

    for i in range(n):
        # 스택의 top에 있는 인덱스 주가가 현재보다 높으면 가격 하락 발생
        while stack and prices[stack[-1]] > prices[i]:
            top = stack.pop()
            answer[top] = i - top   # 걸린 시간 저장

        stack.append(i)

    # 끝까지 가격이 떨어지지 않은 경우 처리
    while stack:
        top = stack.pop()
        answer[top] = n - 1 - top

    return answer


solution([1, 2, 3, 2, 3])