N = int(input())
word = [list(map(str, input())) for _ in range(N)]
origin_word = word[0]
origin_len = len(origin_word)
# 1.두 단어가 같은 구성을 갖는 경우
# 길이가 같고 구성하는게 같으면 끝
# 2.한 단어에서 한 문자를 더하거나, 빼거나
# 더할 때
# 기존보다 길이가 1 작고 기존의 문자열에서 1개 빼고 다 가지고 있는 경우
# 뺄 때 (ok)
# 기존의 길이보다 1 크고 기존의 문자열을 다 충족할 때
# 3.하나의 문자를 다른 문자로 바꾸는는경우
# 길이가 같고 구성하는 문자가 1개 빼고 다 같을 때
ans = 0
dic_orgin = {}
for i in origin_word:
    dic_orgin[i] = 0
for ori in origin_word:
    for key, value in dic_orgin.items():
        if key == ori:
            value += 1
            dic_orgin[key] = value
for wo in word:
    dic = {}
    for i in origin_word:
        dic[i] = 0
# 길이가 더 작은 경우
    if origin_len == (len(wo) + 1):
        for w in wo:
            for key, value in dic.items():
                for k, v in dic_orgin.items():
                    if key == w:
                        value += 1
                        if k == w:
                            if v <= value:
                                dic[key] = v
                            else:
                                dic[key] = value
        if (sum(dic_orgin.values())-1) == sum(dic.values()):
            ans += 1

#길이가 더 큰 경우
    if origin_len == (len(wo) - 1):
        for w in wo:
            for key, value in dic.items():
                for k, v in dic_orgin.items():
                    if key == w:
                        value += 1
                        if k == w:
                            if v <= value:
                                dic[key] = v
                            else:
                                dic[key] = value
        if sum(dic_orgin.values()) == sum(dic.values()):
            ans += 1

    if origin_len == len(wo):
        for w in wo:
            for key, value in dic.items():
                for k, v in dic_orgin.items():
                    if key == w:
                        value += 1
                        if k == w:
                            if v <= value:
                                dic[key] = v
                            else:
                                dic[key] = value

        if (sum(dic_orgin.values())-1) <= sum(dic.values()):
            ans += 1
print(ans-1)