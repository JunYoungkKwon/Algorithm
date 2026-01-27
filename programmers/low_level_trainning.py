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









