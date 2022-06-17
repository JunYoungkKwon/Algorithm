#Python
#요세푸스순열

#공백을 기준으로 입력받고 두 순자를 int형 변환후 각각 저장
N,K = map(int, input().split())

peo = [i for i in range(1, N+1)]
pt = 0
ans = []
for _ in range(N):
    pt += K -1
    pt %= len(peo)
    ans.append(peo.pop(pt))

print(f"<{', '.join(map(str, ans))}>")
