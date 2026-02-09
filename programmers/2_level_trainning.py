# [최댓값과 최솟값]
def solution(s):
    nums = list(map(int, s.split()))
    return str(min(nums)) + " " + str(max(nums))
# [JadenCase 문자열 만들기]
def solution(s):
    s = s.split(" ")
    answer = []
    for i in s:
        if i:
            i = i.lower()
            if i[0].isalpha():
                i = i[0].upper() + i[1:]
            answer.append(i)
        else:
            answer.append(i)
    return " ".join(answer)
# [최솟값 만들기]
def solution(A, B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    for i in range(len(A)):
        answer += A[i] * B[i]
    return answer
# [이진 변환 반복하기]
def solution(s):
    answer = []
    zero_cnt = 0
    bin_cnt = 0
    while len(s) > 1:
        bin_cnt += 1
        zero_cnt += s.count("0")
        s = s.replace("0", "")
        if s == "1":
            return [bin_cnt, zero_cnt]
        a = len(s)
        s = bin(a)[2:]
    return [bin_cnt, zero_cnt]
# [숫자의 표현]
def solution(n):
    answer = 0
    for k in range(1, n + 1):
        base_sum = k * (k - 1) // 2
        if n - base_sum <= 0:
            break

        if (n - base_sum) % k == 0:
            answer += 1

    return answer
# [다음 큰 숫자]
def solution(n):
    result = n
    one_cnt = bin(n)[2:].count("1")
    while True:
        result += 1
        if bin(result)[2:].count("1") == one_cnt:
            return result
# [짝지어 제거하기]
def solution(s):
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    return 1 if not stack else 0
# [피보나치 수]
def solution(n):
    mod = 1234567
    dp =[0] * (n+1)
    dp[0], dp[1] = 0, 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n] % mod
# [카펫]
def solution(brown, yellow):
    total = brown + yellow

    for h in range(1, int(total**0.5) + 1):
        if total % h == 0:
            w = total // h
            if w >= h:
                if (w - 2) * (h - 2) == yellow:
                    return [w, h]
# [구명보트]
def solution(people, limit):
    people.sort()
    left = 0
    right = len(people) - 1
    boat = 0

    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
        right -= 1
        boat += 1
    return boat
# [1]
# [1]
# [1]
# [1]
# [1]
# [1]
# [1]
# [1]
# [1]
# [1]
# [1]
# [1]
# [1]
# [1]
# [1]
# [1]
# [1]
# [1]
# [1]
# [1]
# [1]
# [1]
# [1]
# [1]
# [1]
# [1]
# [1]
# [1]
# [1]
# [1]