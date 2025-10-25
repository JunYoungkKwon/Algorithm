from itertools import combinations

s = input().strip()

# 1. 괄호 쌍 찾기
stack = []
pairs = []
for i, ch in enumerate(s):
    if ch == '(':
        stack.append(i)
    elif ch == ')':
        open_idx = stack.pop()
        pairs.append((open_idx, i))

# 2. 모든 부분집합으로 제거
results = set()
n = len(pairs)
for k in range(1, n+1):
    for comb in combinations(pairs, k):
        to_remove = set()
        for start, end in comb:
            to_remove.add(start)
            to_remove.add(end)
        new_s = ''.join(s[i] for i in range(len(s)) if i not in to_remove)
        results.add(new_s)

# 3. 사전순 출력
for r in sorted(results):
    print(r)
