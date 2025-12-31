from collections import deque


def change_word(ori, t):
    n = len(t)
    dif = 0
    for i in range(n):
        if ori[i] != t[i]:
            dif += 1
    return dif == 1


def solution(begin, target, words):
    answer = 0
    # 타겟의 단어가 words에 없으면  0리턴
    if not target in words:
        return 0
    visited = []

    def bfs(begin_word, cnt):
        deq = deque()
        deq.append((begin_word, cnt))
        while deq:
            word, count = deq.popleft()
            if word == target:
                return count
            for w in words:
                if not w in visited and change_word(word, w):
                    visited.append(w)
                    deq.append((w, count + 1))

        return 0

    return bfs(begin, 0)
