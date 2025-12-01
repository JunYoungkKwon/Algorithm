#입력으로 주어진 첫 번째 단어와 비슷한 단어가 몇 개인지 첫째 줄에 출력

# 두 개의 단어가 같은 종류의 문자로 이루어져 있다.
# 같은 문자는 같은 개수 만큼 있다
#한 단어에서 한 문자를 더하거나, 빼거나,
# 하나의 문자를 다른 문자로 바꾸어 나머지 한 단어와 같은 구성을 갖게 되는 경우

N = int(input()) #단어의 개수
dic = {}
word = input().rstrip()
ans = len(word)
answer = 0
for al in word:
    if al in dic:
        dic[al] += 1
    else:
        dic[al] = 1

for _ in range(N-1):
    si_word = input().rstrip()
    dic2 = {}
    for al in si_word:
        if al in dic2:
            dic2[al] += 1
        else:
            dic2[al] =  1

    # 문자 차이를 체크
    diff = 0

    # 기준 단어 기준으로 차이 계산
    for k in dic:
        if k in dic2:
            diff += abs(dic[k] - dic2[k])
        else:
            diff += dic[k]

    # 비교 단어에만 있는 문자 차이 추가
    for k in dic2:
        if k not in dic:
            diff += dic2[k]

    # 비슷한 단어 조건
    # 길이 같으면: diff <= 2
    # 길이 1 차이면: diff <= 1
    # 그 외는 불가능
    if len(word) == len(si_word):
        if diff <= 2:
            answer += 1
    elif abs(len(word) - len(si_word)) == 1:
        if diff <= 1:
            answer += 1



