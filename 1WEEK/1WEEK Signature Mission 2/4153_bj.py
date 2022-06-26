while True:
    num = list(map(int, input().split()))
    if sum(num) == 0:
        break
    maxNum = max(num)
    num.remove(maxNum)
    if(num[0] ** 2 + num[1] ** 2 == maxNum ** 2 ):
        print("right")
    else:
        print("wrong")

