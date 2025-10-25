N, S = map(int, input().split())
num =  list(map(int, input().split()))
count = 0

def dfs(idx, sum):
    global count
    if N == idx:
        if sum == S:
            count += 1

        return

    #선택해서 +하는 경우
    dfs(idx + 1 , sum + num[idx])
    # 미선택 경우
    dfs(idx + 1 , sum)

#공징합일 경우 -1
if S == 0:
    count -= 1

dfs(0, 0)

print(count)