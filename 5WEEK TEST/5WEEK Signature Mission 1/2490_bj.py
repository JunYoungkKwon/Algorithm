dic = {'A': 3, 'B': 2, 'C': 1, 'D':0,'E':4}

for i in range(3):
    ans = sum(map(int, input().split()))

    for key in dic:
        if dic[key] == ans:
            print(key)