from collections import defaultdict
N = input()
N = N.upper()
li = []
cnt_alpha = defaultdict(int)
for i in N:
    cnt_alpha[i] += 1

for k,v in cnt_alpha.items():
    if max(cnt_alpha.values()) == v:
        li.append(k)
if len(li) >1 :
    print("?")
if len(li) == 1:
    print(*li)



