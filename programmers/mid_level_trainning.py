# [두 수의 합 구하기]
def solution(num1, num2):
    return num1+num2
# [두 수의 차 구하기]
def solution(num1, num2):
    return num1 - num2
# [두 수의 곱 구하기]
def solution(num1, num2):
    return num1 * num2
# [몫 구하기]
def solution(num1, num2):
    return num1 // num2
# [두 수의 나눗셈]
def solution(num1, num2):
    return int((num1 / num2) * 1000)
# [숫자 비교하기]
def solution(num1, num2):
    return 1 if num1 == num2 else -1
# [분수의 덧셈]
import math
def solution(numer1, denom1, numer2, denom2):
    a = numer1 * denom2 + numer2 * denom1
    b = denom1 * denom2
    gcd = math.gcd(a, b)
    return [a//gcd, b//gcd]
# [배열 두배 만들기]
def solution(numbers):
    return [i*2 for i in numbers]
# [나이 출력]
def solution(age):
    return 2023-age
# [나머지 구하기]
def solution(num1, num2):
    return num1 % num2
# [각도기]
def solution(angle):
    if 0 < angle < 90:
        return 1
    elif angle == 90:
        return 2
    elif 90 < angle < 180:
        return 3
    else:
        return 4
# [양꼬치]
def solution(n, k):
    return (12000*n) + (2000*(k-(n // 10))) if n // 10 else (12000*n) + (2000*k)
# [짝수의 합]
def solution(n):
    return sum(i for i in range (0,n+1, 2))
# [배열의 평균값]
def solution(numbers):
    return sum(numbers) / len(numbers)
# [배열 뒤집기]
def solution(num_list):
    return num_list[::-1]
# [뒤집힌 문자열]
def solution(my_string):
    return my_string[::-1]
# [편지]
def solution(message):
    return len(message) * 2
# [피자 나눠 먹기 (1)]
def solution(n):
    for i in range(1, 16):
        if n <= 7*i:
            return i
# [세균 증식]
def solution(n, t):
    return n*(2**(t))
# [최댓값 만들기 (1)]
def solution(numbers):
    numbers.sort()
    return numbers[-1] *numbers[-2]
# [머쓱이보다 키 큰 사람]
def solution(array, height):
    return sum(1 for x in array if x > height)
# [삼각형의 완성조건 (1)]
def solution(sides):
    sides.sort()
    return 1 if sides[-1] < sides[0]+sides[1] else 2
# [배열 자르기]
def solution(numbers, num1, num2):
    return numbers[num1:num2+1]
# [피자 나눠 먹기 (3)]
def solution(slice, n):
    return (n+slice-1)//slice
# [점의 위치 구하기]
def solution(dot):
    x, y = dot
    if y > 0 and x > 0:
        return 1
    elif y > 0 and x < 0:
        return 2
    elif y < 0 and x < 0:
        return 3
    else:
        return 4
# [배열의 유사도]
def solution(s1, s2):
    return len(set(s1) & set(s2))
# [순서쌍의 개수]
def solution(n):
    return sum(1 for i in range(1, n+1) if n%i == 0)
# [n의 배수 고르기]
def solution(n, numlist):
    return [i for i in numlist if i%n == 0]
# [배열 원소의 길이]
def solution(strlist):
    return [len(i) for i in strlist]
# [아이스 아메리카노]
def solution(money):
    return [money//5500, money%5500]
# [문자열안에 문자열]
def solution(str1, str2):
    return 1 if str2 in str1 else 2
# [문자 반복 출력하기]
def solution(my_string, n):
    return ''.join(i * n for i in my_string)
# [제곱수 판별하기]
def solution(n):
    x = int(n ** 0.5)
    return 1 if x * x == n else 2
# [특정 문자 제거하기]
def solution(my_string, letter):
    return my_string.replace(letter, "")
# [모음 제거]
def solution(my_string):
    for v in "aeiou":
        my_string = my_string.replace(v, "")
    return my_string
# [짝수 홀수 개수]
def solution(num_list):
    s = sum(1 for i in num_list if i%2 == 0)
    return [s, len(num_list)-s]
# [자릿수 더하기]
def solution(n):
    return sum(int(i) for i in str(n))
# [숨어있는 숫자의 덧셈 (1)]
def solution(my_string):
    return sum(int(i) for i in my_string if i.isdigit())
# [대문자와 소문자]
def solution(my_string):
    return my_string.swapcase()
# [중복된 숫자 개수]
def solution(array, n):
    return array.count(n)
# [중앙값 구하기]
def solution(array):
    array.sort()
    return array[(len(array)//2)-1] if len(array)%2 == 0 else array[(len(array)//2)]
# [짝수는 싫어요]
def solution(n):
    return [i for i in range(1, n+1, 2)]
# [옷가게 할인 받기]
def solution(price):
    if price >= 500000:
        return int(price * 0.8)
    elif price >= 300000:
        return int(price * 0.9)
    elif price >= 100000:
        return int(price * 0.95)
    else:
        return price
# [직각삼각형 출력하기]
n = int(input())
for i in range(1, n+1):
    print("*"*i)
# [개미 군단]
def solution(hp):
    return hp // 5 + (hp % 5) // 3 + (hp % 5) % 3
# [가위 바위 보]
def solution(rsp):
    answer = ''
    for i in rsp:
        if i == "2":
            answer += "0"
        elif i == "0":
            answer += "5"
        else:
            answer += "2"
    return answer
# [주사위의 개수]
def solution(box, n):
    return (box[0] // n) * (box[1] // n) * (box[2] // n)
# [문자열 정렬하기 (1)]
def solution(my_string):
    return sorted([int(i) for i in my_string if i.isdigit()])
# [최댓값 만들기 (2)]
def solution(numbers):
    numbers.sort()
    return max(numbers[-1] * numbers[-2], numbers[0] * numbers[1])
# [암호 해독]
def solution(cipher, code):
    answer = ''
    for i in range(code-1, len(cipher), code):
        answer += cipher[i]
    return answer
# [인덱스 바꾸기]
def solution(my_string, num1, num2):
    s = list(my_string)
    s[num1], s[num2] = s[num2], s[num1]
    return ''.join(s)
# [약수 구하기]
def solution(n):
    return [i for i in range(1, n+1) if n%i == 0]
# [가장 큰 수 찾기]
def solution(array):
    return [max(array), array.index(max(array))]
# [문자열 정렬하기 (2)]
def solution(my_string):
    a = list(my_string.lower())
    a.sort()
    return "".join(a)
# [숫자 찾기]
def solution(num, k):
    a = str(num)
    return -1 if a.find(str(k)) == -1 else a.find(str(k))+1
# [피자 나눠 먹기 (2)]
def solution(n):
    return next(i for i in range(1, 200) if (6*i) % n == 0)
# [외계행성의 나이]
def solution(age):
    alphabet = 'abcdefghij'
    return ''.join(alphabet[int(d)] for d in str(age))
# [최빈값 구하기]
from collections import Counter
def solution(array):
    count = Counter(array)
    max_freq = max(count.values())
    modes = [num for num, freq in count.items() if freq == max_freq]
    return modes[0] if len(modes) == 1 else -1
# [배열 회전시키기]
from collections import deque
def solution(numbers, direction):
    deq = deque(numbers)
    if direction == "right":
        deq.rotate(1)  # 오른쪽으로 1칸 회전
    else:
        deq.rotate(-1)
    return list(deq)
# [369게임]
from collections import Counter
def solution(order):
    cnt = Counter(str(order))
    return cnt['3'] + cnt['6'] + cnt['9']
# [합성수 찾기]
def solution(n):
    ans = 0
    for i in range(1, n + 1):
        cnt = 0
        for a in range(1, i + 1):
            if i % a == 0:
                cnt += 1
        if cnt >= 3:
            print(i)
            ans += 1
    return ans
# [중복된 문자 제거]
def solution(my_string):
    ans = []
    for i in my_string:
        if not i in ans:
            ans.append(i)
    return "".join(ans)
# [2차원으로 만들기]
def solution(num_list, n):
    return [num_list[i:i+n] for i in range(0, len(num_list), n)]
# [모스부호 (1)]
def solution(letter):
    morse = {
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'}
    answer = ''
    letter = letter.split()
    for i in letter:
        answer += morse[i]
    return answer
# [A로 B 만들기]
def solution(before, after):
    before = sorted(list(before))
    after = sorted(list(after))
    return 1 if before == after else 0
# [k의 개수]
def solution(i, j, k):
    count = 0
    for num in range(i, j+1):
        count += str(num).count(str(k))
    return count
# [한 번만 등장한 문자]
from collections import Counter
def solution(s):
    cnt = Counter(s)
    answer = []
    print(cnt)
    for k, v in cnt.items():
        if v == 1:
            answer.append(k)
    return "".join(sorted(answer))
# [숨어있는 숫자의 덧셈 (2)]
def solution(my_string):
    ans = 0
    a = ""
    for i in my_string:
        if i.isdigit():
            a += i  # 숫자를 이어붙이기
        else:
            if a:  # a가 빈 문자열이 아니면
                ans += int(a)
                a = ""  # 초기화
    if a:  # 마지막에 남은 숫자 처리
        ans += int(a)
    return ans
# [7의 개수]
from collections import Counter
def solution(array):
    result = "".join(map(str, array))
    cnt = Counter(result)
    return cnt['7']
# [진료 순서 정하기]
def solution(emergency):
    sorted_emergency = sorted(emergency, reverse=True)
    return [sorted_emergency.index(x)+1 for x in emergency]
# [가까운 수]
def solution(array, n):
    answer = 999
    diff = 999
    for i in array:
        if abs(n - i) < diff:
            answer = i
            diff = abs(n - i)
        elif abs(n - i) == diff:
            answer = min(i, answer)

    return answer
# [팩토리얼]
import math
def solution(n):
    i = 1
    while math.factorial(i) <= n:
        i += 1
    return i-1
# [잘라서 배열로 저장하기]
def solution(my_str, n):
    return [my_str[i:i+n] for i in range(0, len(my_str), n)]
# [컨트롤 제트]
def solution(s):
    s = s.split()
    answer = 0
    num = 0
    print(s)
    for i in s:
        if i == "Z":
            answer -= num

        else:
            answer += int(i)
            num = int(i)

    return answer
# [소인수분해]
def solution(n):
    answer = []
    i = 2  # 소수는 2부터 시작
    while i * i <= n:  # i*i <= n까지만 확인해도 충분
        if n % i == 0:
            answer.append(i)
            while n % i == 0:
                n //= i
        i += 1
    if n > 1:  # 마지막으로 남은 소수 처리
        answer.append(n)
    return answer
# [문자열 계산하기]
def solution(my_string):
    stk = []
    a = my_string.split()
    pm = 1
    for i in a:
        if i == "+":
            pm = 1
        elif i == "-":
            pm = -1
        else:
            if pm == -1:
                stk.append(-int(i))
            else:
                stk.append(int(i))
    return sum(stk)
# [공 던지기]
def solution(numbers, k):
    idx = 0
    for _ in range(k-1):
        idx = (idx + 2) % len(numbers)
    return numbers[idx]
# [영어가 싫어요]
def solution(numbers):
    num_dict = {
        "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
        "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
    }
    for word, digit in num_dict.items():
        numbers = numbers.replace(word, digit)
    return int(numbers)
# [삼각형의 완성조건 (2)]
def solution(sides):
    a, b = sorted(sides)
    return (a + b - 1) - (b - a)
















