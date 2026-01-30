# [덧셈식 출력하기]
a, b = map(int, input().strip().split(' '))
print(f"{a} + {b} = {a+b}")
# [문자열 붙여서 출력하기]
str1, str2 = input().strip().split(' ')
print("".join(str1+str2))
# [문자열 돌리기]
str = input()
for s in str:
    print(s)
n = int(input())
# [홀짝 구분하기]
if n % 2 == 0:
    print(f"{n} is even")
else:
    print(f"{n} is odd")
# [문자열 겹쳐쓰기]
def solution(my_string, overwrite_string, s):
    answer = ''
    answer += my_string[:s]
    answer += overwrite_string
    answer += my_string[s + len(overwrite_string):]
    return answer
# [문자열 섞기]
def solution(str1, str2):
    answer = ''
    for i in range(len(str1)):
        answer += str1[i]
        answer += str2[i]
    return answer
# [문자 리스트를 문자열로 변환하기]
def solution(arr):
    answer = "".join(arr)
    return answer
# [문자열 곱하기]
def solution(my_string, k):
    answer = my_string*int(k)
    return answer
# [더 크게 합치기]
def solution(a, b):
    return max(int(str(a) + str(b)), int(str(b) + str(a)))
# [두 수의 연산값 비교하기]
def solution(a, b):
    return max(int(str(a)+str(b)), 2*a*b)
# [n의 배수]
def solution(num, n):
    return 1 if (num % n) == 0 else 0
# [공배수]
def solution(number, n, m):
    return 1 if number % n == 0 and number % m == 0 else 0
# [홀짝에 따라 다른 값 반환하기]
def solution(n):
    ans = 0
    if n % 2 == 0:
        for num in range(0, n+1, 2):
            ans += num*num
    else:
        for num in range(1, n+1, 2):
            ans += num
    return ans
# [조건 문자열]
def solution(ineq, eq, n, m):
    if ineq == "<" and eq == "=":
        return int(n <= m)
    if ineq == "<" and eq == "!":
        return int(n < m)
    if ineq == ">" and eq == "=":
        return int(n >= m)
    if ineq == ">" and eq == "!":
        return int(n > m)
# [flag에 따라 다른 값 반환하기]
def solution(a, b, flag):
    return (a+b) if flag else a-b
# [문자열의 뒤의 n글자]
def solution(my_string, n):
    return my_string[-n:]
# [원소들의 곱과 합]
def solution(num_list):
    a = 1
    for n in num_list:
        a *= n
    return 1 if a < sum(num_list) ** 2 else 0
# [접미사인지 확인하기]
def solution(my_string, is_suffix):
    return 1 if my_string.endswith(is_suffix) else 0
# [n 번째 원소까지]
def solution(num_list, n):
    return num_list[:n]
# [접두사인지 확인하기]
def solution(my_string, is_prefix):
    return 1 if my_string.startswith(is_prefix) else 0
# [글자 이어 붙여 문자열 만들기]
def solution(my_string, index_list):
    answer = ''
    for n in index_list:
        answer += my_string[n]
    return answer
# [콜라츠 수열 만들기]
def solution(n):
    def chk(num):
        if num % 2 == 0:
            return True
        else:
            return False
    answer = []
    while True:
        answer.append(n)
        if n == 1:
            return answer
        if chk(n):
            n /= 2
        else:
            n = 3 * n + 1
    return answer
# [주사위 게임 2]
def solution(a, b, c):
    nums = [a, b, c]
    cnt = len(set(nums))

    if cnt == 3:      # 모두 다름
        return sum(nums)
    elif cnt == 2:    # 두 개 같음
        return sum(nums) * sum(n*n for n in nums)
    else:             # 모두 같음
        return sum(nums) * sum(n*n for n in nums) * sum(n**3 for n in nums)
# [특정한 문자를 대문자로 바꾸기]
def solution(my_string, alp):
    answer = ''
    for i in my_string:
        if i == alp:
            i = i.upper()

        answer += i
    return answer
# [n개 간격의 원소들]
def solution(num_list, n):
    answer = []
    for i in range(0, len(num_list), n):
        answer.append(num_list[i])
    return answer
# [조건에 맞게 수열 변환하기 3]
def solution(arr, k):
    if k % 2 == 1:
        return [x * k for x in arr]
    else:
        return [x + k for x in arr]
# [l로 만들기]
def solution(myString):
    return ''.join("l" if x < "l" else x for x in myString)
# [배열 조각하기]
def solution(arr, query):
    ans = arr
    for i, id in enumerate(query):
        if i % 2 == 0:
            ans = ans[:id + 1]
        else:
            ans = ans[id:]

    return ans
# [코드 처리하기]
def solution(code):
    answer = ''
    mode = 0
    for idx, n in enumerate(code):
        if n == "1":
            mode = 1 - mode
            continue
        if mode == 0 and n != "1" and idx%2 == 0:
            answer += n
        if mode == 1 and n != "1" and idx%2 != 0:
            answer += n
    return answer if answer else "EMPTY"
# [등차수열의 특정한 항만 더하기]
def solution(a, d, included):
    answer = 0
    for i, tf in enumerate(included):
        if tf:
            answer += a+(d*i)
    return answer
# [이어 붙인 수]
def solution(num_list):
    answer = 0
    holsu = ""
    jjacksu = ""
    for i in num_list:
        if i % 2 == 0:
            jjacksu += str(i)
        else:
            holsu += str(i)
    return int(jjacksu) + int(holsu)
# [마지막 두 원소]
def solution(num_list):
    if num_list[-1] > num_list[-2]:
        num_list.append(num_list[-1] - num_list[-2])

    elif num_list[-1] <= num_list[-2]:
        num_list.append(num_list[-1] * 2)

    return num_list
# [수 조작하기 1]
def solution(n, control):
    answer = n
    for wasd in control:
        if wasd == "w":
            answer += 1
        elif wasd == "s":
            answer -= 1
        elif wasd == "d":
            answer += 10
        else:
            answer -= 10
    return answer
# [수 조작하기 2]
def solution(numLog):
    now = 0
    answer = ''
    for i in range(len(numLog)-1):
        if numLog[i+1] - numLog[i] == 1:
            answer += "w"
        elif numLog[i+1] - numLog[i] == 10:
            answer += "d"
        elif numLog[i+1] - numLog[i] == -1:
            answer += "s"
        else:
            answer += "a"
    return answer
# [수열과 구간 쿼리 3]
def solution(arr, queries):
    answer = []
    for i, j in queries:
        arr[i], arr[j] = arr[j], arr[i]

    return arr
# [수열과 구간 쿼리 2]
def solution(arr, queries):
    result = []
    for s, e, k in queries:
        # s부터 e까지 범위 정렬하지 않고 필터
        candidates = [num for num in arr[s:e+1] if num > k]
        if candidates:
            result.append(min(candidates))
        else:
            result.append(-1)
    return result
# [카운트 업]
def solution(start_num, end_num):
    return [i for i in range(start_num, end_num+1)]
# [n 번째 원소부터]
def solution(num_list, n):
    return num_list[n-1:]
# [주사위 게임 2]
def solution(a, b, c):
    nums = [a, b, c]
    unique = len(set(nums))

    s1 = a + b + c
    s2 = a * a + b * b + c * c
    s3 = a * a * a + b * b * b + c * c * c

    if unique == 3:  # 모두 다름
        return s1
    elif unique == 2:  # 두 개만 같음
        return s1 * s2
    else:  # 모두 같음
        return s1 * s2 * s3
# [정수 부분]
def solution(flo):
    return int(flo)
# [문자열 바꿔서 찾기]
def solution(myString, pat):
    ans = ""
    for i in myString:
        if i == "A":
            ans += "B"
        else:
            ans += "A"
    return 1 if pat in  ans else 0
# [정수 찾기]
def solution(num_list, n):
    return 1 if n in num_list else 0
# [배열의 원소 삭제하기]
def solution(arr, delete_list):
    delete_set = set(delete_list)
    return [x for x in arr if x not in delete_list]
# [꼬리 문자열]
def solution(str_list, ex):
    ans = [a for a in str_list if ex not in a]
    return "".join(ans)
# [0 떼기]
def solution(n_str):
    return n_str.lstrip("0")
# [부분 문자열]
def solution(str1, str2):
    return 1 if str1 in str2 else 0
# [부분 문자열인지 확인하기]
def solution(my_string, target):
    return 1 if target in my_string else 0
# [문자열로 변환]
def solution(n):
    return str(n)
# [뒤에서 5등 위로]
def solution(num_list):
    num_list.sort()
    return num_list[5:]
# [문자열 정수의 합]
def solution(num_str):
    answer = 0
    for i in num_str:
        answer += int(i)
    return answer
# [문자열을 정수로 변환]
def solution(n_str):
    return int(n_str)
# [뒤에서 5등까지]
def solution(num_list):
    num_list.sort()
    return num_list[:5]
# [배열의 길이에 따라 다른 연산하기]
def solution(arr, n):
    answer = []
    if len(arr) % 2 == 0:
        for i, num in enumerate(arr):
            if i % 2 != 0:
                answer.append(num + n)
            else:
                answer.append(num)
    else:
        for i, num in enumerate(arr):
            if i % 2 == 0:
                answer.append(num + n)
            else:
                answer.append(num)

    return answer
# [배열 비교하기]
def solution(arr1, arr2):
    answer = 0
    if len(arr1) != len(arr2):
        return 1 if len(arr1) > len(arr2) else -1
    else:
        if sum(arr1) > sum(arr2):
            return 1
        elif sum(arr1) < sum(arr2):
            return -1
        else:
            return 0
# [주사위 게임 1]
def solution(a, b):
    a_ck = (0 if a % 2 == 0 else 1)
    b_ck = (0 if b % 2 == 0 else 1)

    if a_ck + b_ck == 2:
        return a ** 2 + b ** 2
    elif a_ck + b_ck == 1:
        return 2 * (a + b)
    else:
        return abs(a - b)
# [ad 제거하기]
def solution(strArr):
    answer = []
    for a in strArr:
        if "ad" not in a:
            answer.append(a)
    return answer
# [배열의 원소만큼 추가하기]
def solution(arr):
    answer = []
    for i in arr:
        for a in range(i):
            answer.append(i)
    return answer
# [x 사이의 개수]
def solution(myString):
    return [len(s) for s in myString.split('x')]
# [홀수 vs 쩍수]
def solution(num_list):
    odd_sum = sum(num_list[0::2])   # 1,3,5,...
    even_sum = sum(num_list[1::2])  # 2,4,6,...
    return max(odd_sum, even_sum)
# [공백으로 구분하기 2]
def solution(my_string):
    return my_string.split()
# [rny_string]
def solution(rny_string):
    return rny_string.replace("m", "rn")
# [공백으로 구분하기 1]
def solution(my_string):
    return my_string.split()
# [배열에서 문자열 대소문자 변환하기]
def solution(strArr):
    return [a.lower() if i % 2 == 0 else a.upper() for i, a in enumerate(strArr) ]
# [수열과 구간 쿼리 4]
def solution(arr, queries):
    for s, e, k in queries:
        for i in range(s, e+1):
            if i%k == 0:
                arr[i] += 1
    return arr
# [배열 만들기 2]
def solution(l, r):
    answer = []
    for i in range(l, r+1):
        if all(k in "05" for k in str(i)):
            answer.append(i)
    return answer if answer else [-1]
# [대문자로 바꾸기]
def solution(myString):
    return myString.upper()
# [배열 만들기 4]
def solution(arr):
    stk = []
    i = 0
    while i < len(arr):
        if not stk:
            stk.append(arr[i])
            i += 1
        else:
            if stk[-1] < arr[i]:
                stk.append(arr[i])
                i += 1
            else:
                stk.pop()
    return stk
# [간단한 논리 연산]
def solution(x1, x2, x3, x4):
    return (x1 or x2) and (x3 or x4)
# [주사위 게임 3]
def solution(a, b, c, d):
    nums = [a, b, c, d]
    nums.sort()
    if nums[0] == nums[3]:
        return 1111 * nums[0]
    if nums[0] == nums[2] or nums[1] == nums[3]:
        if nums[0] == nums[2]:
            p, q = nums[0], nums[3]
        else:
            p, q = nums[1], nums[0]
        return (10 * p + q) ** 2
    if nums[0] == nums[1] and nums[2] == nums[3]:
        return (nums[0] + nums[2]) * abs(nums[0] - nums[2])

    if nums[0] == nums[1]:
        return nums[2] * nums[3]
    if nums[1] == nums[2]:
        return nums[0] * nums[3]
    if nums[2] == nums[3]:
        return nums[0] * nums[1]
    return nums[0]
# [9로 나눈 나머지]
def solution(number):
    return int(number) % 9
# [문자열 여러 번 뒤집기]
def solution(my_string, queries):
    for s, e in queries:
        my_string = (
            my_string[:s] +
            my_string[s:e+1][::-1] +
            my_string[e+1:]
        )
    return my_string
# [간단한 식 계산하기]
def solution(binomial):
    a, op, b = binomial.split()
    print(binomial.split())
    a, b = int(a), int(b)

    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    else:  # '*'
        return a * b
# [소문자로 바꾸기]
def solution(myString):
    return myString.lower()
# [가까운 1 찾기]
def solution(arr, idx):
    for i in range(idx, len(arr)):
        if arr[i] == 1:
            return i
    return -1
# [원하는 문자열 찾기]
def solution(myString, pat):
    return 1 if pat.lower() in myString.lower() else 0
# [배열 만들기 3]
def solution(arr, intervals):
    answer = []
    for s, e in intervals:
        for i in arr[s:e+1]:
            answer.append(i)
    return answer
# [길이에 따른 연산]
def solution(num_list):
    answer = 1
    if len(num_list) >= 11:
        return sum(num_list)
    else:
        for i in num_list:
            answer *= i
        return answer
# [조건에 맞게 수열 변환하기 1]
def solution(arr):
    answer = []
    for i in arr:
        if i >= 50 and i % 2 == 0:
            answer.append(i // 2)

        elif i < 50 and i % 2 != 0:
            answer.append(i * 2)
        else:
            answer.append(i)
    return answer
# [할 일 목록]
def solution(todo_list, finished):
    return [todo_list[a] for a, i in enumerate(finished) if not i]
# [n보다 커질 때까지 더하기]
def solution(numbers, n):
    answer = 0
    for i in numbers:
        if answer > n:
            return answer
        answer += i
    return answer
# [순서 바꾸기]
def solution(num_list, n):
    return num_list[n:] + num_list[:n]
# [A 강조하기]
def solution(myString):
    return myString.lower().replace("a", "A")
# [5명씩]
def solution(names):
    answer = []
    for i in range(0,len(names),5):
        answer.append(names[i])
    return answer
# [배열 만들기 1]
def solution(n, k):
    return [i for i in range(1, n+1) if i % k == 0]
# [부분 문자열 이어 붙여 문자열 만들기]
def solution(my_strings, parts):
    answer = ''
    i = 0
    for s, e in parts:
        a = my_strings[i]
        answer += a[s:e + 1]
        i += 1
    return answer
# [카운트 다운]
def solution(start_num, end_num):
    return [i for i in range(start_num, end_num-1, -1)]
# [접미사 배열]
def solution(my_string):
    answer = []
    for i in range(len(my_string), -1, -1):
        if my_string[i:len(my_string)]:
            answer.append(my_string[i:len(my_string)])
    answer.sort()
    return answer
# [특별한 이차원 배열2]
def solution(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] != arr[j][i]:
                return 0
    return 1
# [특별한 이차원 배열1]
def solution(n):
    answer = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                answer[i][j] = 1
    return answer
# [문자열 잘라서 정렬하기]
def solution(myString):
    return sorted(s for s in myString.split('x') if s)
# [첫 번째로 나오는 음수]
def solution(num_list):
    for i, n in enumerate(num_list):
        if n < 0:
            return i
    return -1
# [이차원 배열 대각선 순회하기]
def solution(board, k):
    answer = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if i + j <= k:
                answer += board[i][j]

    return answer





