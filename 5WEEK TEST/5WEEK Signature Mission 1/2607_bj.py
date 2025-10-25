from collections import Counter
import sys
input = sys.stdin.readline

N = int(input().strip())
base = input().strip()
base_cnt = Counter(base)
print(base_cnt)

ans = 0
for _ in range(N - 1):
    w = input().strip()
    w_cnt = Counter(w)

    # 모든 문자에 대한 차이합 계산
    chars = set(base_cnt.keys()) | set(w_cnt.keys())
    total_diff = sum(abs(base_cnt[ch] - w_cnt[ch]) for ch in chars)

    # 판정: 동일(0), 삽입/삭제(1), 교체(2 & 길이 같음)
    if total_diff <= 1 or (total_diff == 2 and len(base) == len(w)):
        ans += 1

print(ans)
