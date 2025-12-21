from itertools import product
def solution(word):
    li = []
    for i in range(1,6):
        for pro in product(['A', 'E', 'I', 'O', 'U'], repeat=i):
            a = "".join(pro)
            li.append(a)
    li.sort()
    return li.index(word)+1