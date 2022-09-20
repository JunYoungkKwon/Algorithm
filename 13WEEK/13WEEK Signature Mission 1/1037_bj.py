N = int(input())
arr = list(map(int, input().split()))
if N == 1:
    print(arr[0]**2)
else:
    arr.sort()
    print(arr[0]*arr[-1])
