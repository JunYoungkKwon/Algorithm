# [짝수와 홀수]
def solution(num):
    return "Even" if num % 2 == 0 else "Odd"
# [평균 구하기]
def solution(arr):
    return sum(arr) / len(arr)
# [평균 구하기]
def solution(x, n):
    return [x * i for i in range(1, n + 1)]
# [나머지가 1이 되는 수 찾기]
def solution(n):
    for i in range(2, n):
        if n % i == 1:
            return i
# [문자열을 정수로 바꾸기]
def solution(s):
    return int(s)
# [약수의 합]
def solution(n):
    ans = 0
    for i in range(1, n+1):
        if n % i == 0:
            ans += i
    return ans
# [정수 내림차순으로 배치하기]
def solution(n):
    a = sorted(str(n), reverse = True)
    return int("".join(a))
# [하샤드 수]
def solution(x):
    digit_sum = sum(int(d) for d in str(x))
    return x % digit_sum == 0
# [정수 제곱근 판별]
def solution(n):
    root = int(n ** 0.5)
    return (root+1) ** 2 if root**2 == n else -1
# [자연수 뒤집어 배열로 만들기]
def solution(n):
    return [int(i) for i in str(n)][::-1]
# [자릿수 더하기]
def solution(n):
    return  sum(int(i) for i in str(n))
# [두 정수 사이의 합]
def solution(a, b):
    return sum(i for i in range(min(a, b), max(a, b)+1))
# [문자열 내 p와 y의 개수]
from collections import Counter
def solution(s):
    cnt = Counter(s.lower())
    return True if cnt["p"] == cnt["y"] else False
# [음양 더하기]
def solution(absolutes, signs):
    return  sum(absolutes[i] if tf else -absolutes[i] for i, tf in enumerate(signs) )
# [없는 숫자 더하기]
def solution(numbers):
    return 45 - sum(numbers)
# [나누어 떨어지는 숫자 배열]
def solution(arr, divisor):
    return sorted([i for i in arr if i % divisor == 0]) if sorted([i for i in arr if i % divisor == 0]) else [-1]
# [서울에서 김서방 찾기]
def solution(seoul):
    return f"김서방은 {seoul.index('Kim')}에 있다"
# [콜라츠 추측]
def solution(num):
    answer = 0
    while answer <= 500:
        if num == 1:
            return answer
        if num % 2 == 0:
            num //= 2
        else:
            num = (num * 3) + 1
        answer += 1
    return -1
# [핸드폰 번호 가리기]
def solution(phone_number):
    return "*" * (len(phone_number)-4) + phone_number[-4:]
# [가운데 글자 가져오기]
def solution(s):
    return s[(len(s) // 2)]if len(s) % 2 != 0 else s[(len(s) // 2)-1:(len(s) // 2)+1]
# [제일 작은 수 제거하기]
def solution(arr):
    if len(arr) == 1:
        return [-1]
    else:
        arr.remove(min(arr))
        return arr
# [내적]
def solution(a, b):
    return sum(x * y for x, y in zip(a, b))
# [수박수박수박수박수박수?]
def solution(n):
    su = n%2
    i = n//2
    return "수박"*i + "수" * su
# [약수의 개수와 덧셈]
def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        chk = 0
        for j in range(1, i+1):
            if i % j  == 0:
                print(j)
                chk += 1
        if chk % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer
# [문자열 내림차순으로 배치하기]
def solution(s):
    return "".join(sorted(s, reverse = True))
# [부족한 금액 계산하기]
def solution(price, money, count):
    return 0 if money >= sum(i*price for i in range(1, count+1)) else sum(i*price for i in range(1, count+1)) - money
# [문자열 다루기 기본]
def solution(s):
    return (len(s) == 4 or len(s) == 6) and s.isdigit()
# [행렬의 덧셈]
def solution(arr1, arr2):
    answer = []
    for a,b in zip(arr1, arr2):
        k = []
        for i in range(len(arr1[0])):
            k.append(a[i]+b[i])
        answer.append(k)
    return answer
# [직사각형 별찍기]
a, b = map(int, input().strip().split(' '))
for i in range(b):
    print("*"*a)
# [최대공약수와 최소공배수]
import math
def solution(n, m):
    gcd = math.gcd(n ,m)
    return [gcd, (n * m) // gcd]
# [크기가 작은 부분문자열]
def solution(t, p):
    ans = 0
    for i in range(len(t)):
        if int(t[i:(i+len(p))]) <= int(p) and len(t[i:(i+len(p))]) == len(p):
            ans += 1
    return ans
# [예산]
def solution(d, budget):
    ans = 0
    total = 0
    d = sorted(d)
    for i in d:
        if total + i <= budget:
            total += i
            ans+= 1
        else:
            return ans
    return ans
# [3진법 뒤집기]
def solution(n):
    a = ""
    while n >0:
        a += str(n % 3)
        n //= 3
    return int(a, 3)
# [삼총사]
from itertools import combinations
def solution(number):
    answer = 0
    for i in combinations(number, 3):
        if sum(i) == 0:
            answer += 1
    return answer
# [이상한 문자 만들기]
def solution(s):
    s = s.split(" ")
    ans = []
    for i in s:
        text = ""
        for n, eng in enumerate(i):
            if n % 2 == 0:
                text += eng.upper()
            else:
                text += eng.lower()
        ans.append(text)

    return " ".join(ans)
# [가장 가까운 같은 글자]
def solution(s):
    answer = []
    last_pos = {}
    for i, char in enumerate(s):
        if char not in last_pos:
            answer.append(-1)
        else:
            answer.append(i - last_pos[char])
        last_pos[char] = i
    return answer
# [시저 암호]
def solution(s, n):
    answer = ''
    for i in s:
        if i == " ":
            answer += " "
            continue
        base = ord("A") if i.isupper() else ord("a")
        shift = (ord(i) - base + n) % 26 + base
        answer += chr(shift)
    return answer
# [두 개 뽑아서 더하기]
from itertools import combinations
def solution(numbers):
    s= set()
    for i in combinations(numbers, 2):
        s.add(sum(i))
    return sorted(list(s))
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
