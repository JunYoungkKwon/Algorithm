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
# [귤 고르기]
from collections import Counter
def solution(k, tangerine):
    answer = 0
    counts = Counter(tangerine)
    sorted_counts = sorted(counts.values(), reverse=True)
    for count in sorted_counts:
        k -= count
        answer += 1
        if k <= 0:
            break
    return answer
# [점프와 순간 이동]
def solution(n):
    ans = 0
    while n > 0:
        if n % 2 != 0:
            ans += 1
            n -= 1
        else:
            n //= 2
    return ans
# [N개의 최소공배수]
from math import gcd
def solution(arr):
    answer = arr[0]
    for i in range(1, len(arr)):
        answer = (answer * arr[i]) // gcd(answer, arr[i])
    return answer
# [멀리 뛰기]
def solution(n):
    if n <= 2:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    mod = 1234567

    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % mod
    return dp[n]
# [연속 부분 수열 합의 개수]
def solution(elements):
    n = len(elements)
    extended_elements = elements * 2
    sums = set()
    for length in range(1, n + 1):
        for i in range(n):
            sub_sum = sum(extended_elements[i : i + length])
            sums.add(sub_sum)
    return len(sums)
# [영어 끝말잇기]
def solution(n, words):
    answer = []
    for i,word in enumerate(words):
        if not answer:
            answer.append(word)
        else:
            if answer[-1][-1] != word[0] or word in answer:
                return [n, (i+1)//n] if (i+1) % n == 0 else [(i+1) % n, ((i+1)//n)+1]
            else:
                answer.append(word)
    return [0,0]
# [예상 대진표]
def solution(n, a, b):
    answer = 0
    while a != b:
        if (a % 2) == 0:
            a //= 2
        else:
            a = (a // 2) + 1
        if (b % 2) == 0:
            b //= 2
        else:
            b = (b // 2) + 1
        answer += 1
    return answer
# [할인 행사]
def solution(want, number, discount):
    answer = 0
    for i in range(0, len(discount)-9):
        li = discount[i:i+10]
        tf = True
        for i in range(len(number)):
            if li.count(want[i]) != number[i]:
                tf = False
                break
        if tf:
            answer += 1
    return answer
# [완주하지 못한 선수]
from collections import Counter
def solution(participant, completion):
    diff = Counter(participant) - Counter(completion)
    for n, v in diff.items():
        return n

# [폰켓몬]
from itertools import combinations
def solution(nums):
    s = list(set(nums))
    return min(len(s), len(nums)//2)
    # for i in combinations(nums, len(nums)//2):
    #     s.add(list(i))
    #     print(s)
    # answer = 0
    # return answer
# [전화번호 목록]
def solution(phone_book):
    numbers = set(phone_book)
    for number in phone_book:
        for i in range(1, len(number)):
            if number[:i] in numbers:
                return False
    return True
# [의상]
from collections import defaultdict
def solution(clothes):
    dic = defaultdict(list)

    # 종류별로 옷 모으기
    for name, type_ in clothes:
        dic[type_].append(name)

    # 모든 조합 계산
    answer = 1
    for type_ in dic:
        answer *= (len(dic[type_]) + 1)  # (그 종류의 옷 개수 + 안입는 선택지)

    return answer - 1  # 모두 안 입는 경우 제거

# [베스트앨범]
from collections import defaultdict
def solution(genres, plays):
    genre_play_sum = defaultdict(int)     # 장르별 총 재생 횟수
    songs = defaultdict(list)             # 장르별 (재생수, 고유번호)

    # 1. 장르별 총 재생 수 및 노래 리스트 저장
    for i in range(len(genres)):
        genre_play_sum[genres[i]] += plays[i]
        songs[genres[i]].append((plays[i], i))


    # 2. 장르 총 재생 횟수로 내림차순 정렬
    sorted_genres = sorted(genre_play_sum.items(), key=lambda x: -x[1])


    answer = []
    key = lambda x: x[0]

    # 3. 각 장르에서 재생수 기준으로 내림차순, 같으면 고유번호 오름차순
    for genre, _ in sorted_genres:
        sorted_songs = sorted(songs[genre], key=lambda x: (-x[0], x[1]))
        # 상위 2개까지 넣기
        for play, idx in sorted_songs[:2]:
            answer.append(idx)

    return answer
# [같은 숫자는 싫어]
arr = [1,1,3,3,0,1,1]
def solution(arr):
    answer = []
    for v in arr:
        if not answer or answer[-1] != v:
            answer.append(v)
    return answer
solution(arr)
# [기능개발]
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
    return answer
# [올바른 괄호]
def solution(s):
    stk = []
    answer = True
    for i in s:
        if i == "(":
            stk.append(i)
        else:
            if stk:
                stk.pop()
            else:
                return False
    if stk:
        return False
    else:
        return True
# [프로세스]
from collections import deque

def solution(priorities, location):
    deq = deque((p, i) for i, p in enumerate(priorities))
    ans = []

    while deq:
        p, l = deq.popleft()
        # 남아있는 프로세스 중 더 높은 우선순위가 있다면
        if deq and p < max(x[0] for x in deq):
            deq.append((p, l))  # 뒤로 보냄
        else:
            ans.append(l)
            if l == location:  # 목표 위치 프로세스면 종료
                return len(ans)
# [다리를 지나는 트럭]
from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0] * bridge_length)  # 다리 위 상태 (길이만큼 0으로 초기화)
    current_weight = 0                   # 현재 다리 위 총 무게

    for truck in truck_weights:
        while True:
            time += 1
            out = bridge.popleft()       # 한 칸 앞으로 이동
            current_weight -= out

            # 트럭이 올라갈 수 있으면
            if current_weight + truck <= weight:
                bridge.append(truck)     # 트럭 올리기
                current_weight += truck
                break
            else:
                # 못 올라가면 0을 넣고 시간만 흐르게 하기
                bridge.append(0)

    # 마지막 트럭이 완전히 건너는 시간 추가
    time += bridge_length

    return time
# [주식가격]
def solution(prices):
    n = len(prices)
    answer = [0] * n
    stack = []  # 가격이 떨어지지 않은 '인덱스'를 담는 통

    for i in range(n):
        # 1. 스택이 비어있지 않고, 현재 가격이 스택 맨 위 가격보다 떨어졌다면
        while stack and prices[i] < prices[stack[-1]]:
            top = stack.pop()
            # 2. 떨어진 시점(i) - 들어온 시점(top) = 버틴 기간
            answer[top] = i - top

        # 3. 현재 시점의 인덱스를 스택에 추가
        stack.append(i)

    # 4. 끝까지 가격이 떨어지지 않은 나머지 친구들 처리
    while stack:
        top = stack.pop()
        answer[top] = (n - 1) - top

    return answer
# [더 맵게]
import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0

    while len(scoville) >= 2:
        min_num = heapq.heappop(scoville)

        # 제일 작은 값이 이미 K 이상이면 끝
        if min_num >= K:
            return answer

        # 두 번째 최소값 꺼냄
        second_min = heapq.heappop(scoville)
        new_scoville = min_num + second_min * 2
        heapq.heappush(scoville, new_scoville)
        answer += 1

    # 마지막 하나만 남은 경우 처리
    # 하나 남아 있는데 그 값도 K보다 작으면 실패
    if scoville and scoville[0] >= K:
        return answer
    else:
        return -1
# [이중우선순위큐]
import heapq


def solution(operations):
    min_h = []  # 최소 힙
    max_h = []  # 최대 힙
    # 각 숫자가 현재 큐에 존재하는지 확인하는 체크 리스트 (고유 ID 사용)
    visited = [False] * 1000001

    for i, op in enumerate(operations):
        cmd, val = op.split()
        num = int(val)

        if cmd == 'I':
            # 1. 삽입: 두 힙에 모두 넣고, i번째 데이터가 유효함을 표시
            heapq.heappush(min_h, (num, i))
            heapq.heappush(max_h, (-num, i))
            visited[i] = True

        elif cmd == 'D':
            if num == 1:  # 최대값 삭제
                # 2. 이미 삭제된 허수(유령 데이터)들을 힙의 꼭대기에서 제거
                while max_h and not visited[max_h[0][1]]:
                    heapq.heappop(max_h)
                if max_h:
                    _, idx = heapq.heappop(max_h)
                    visited[idx] = False  # 해당 데이터 삭제 처리
            else:  # 최솟값 삭제
                while min_h and not visited[min_h[0][1]]:
                    heapq.heappop(min_h)
                if min_h:
                    _, idx = heapq.heappop(min_h)
                    visited[idx] = False

    # 3. 모든 명령 종료 후, 각 힙의 꼭대기에 있는 유령 데이터 최종 청소
    while max_h and not visited[max_h[0][1]]:
        heapq.heappop(max_h)
    while min_h and not visited[min_h[0][1]]:
        heapq.heappop(min_h)

    # 4. 결과 반환
    if not max_h or not min_h:
        return [0, 0]
    return [-max_h[0][0], min_h[0][0]]
# [1]
# [1]
# [1]
# [1]
# [1]
# [1]
# [1]
# [1]