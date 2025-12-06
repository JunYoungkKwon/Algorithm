from collections import defaultdict

clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]

def solution(clothes):
    dic = defaultdict(list)

    for a, b in clothes:
        dic[b].append(a)

    print(dic)


solution(clothes)


