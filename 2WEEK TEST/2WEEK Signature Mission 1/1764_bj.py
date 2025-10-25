N, M = map(int, input().split())
no_hear = set()
no_see = set()
for _ in range(N):
    no_hear.add(input())

for _ in range(M):
    no_see.add(input())

no_hear_see = no_see & no_hear
no_hear_see = sorted(no_hear_see)
print(len(no_hear_see))
for ch in no_hear_see:
    print(ch)


