N = int(input())
money = list(map(int, input().split()))
total_budget = int(input())

low = 1
high = max(money)
max_mid = 0

if sum(money) <= total_budget:
    print(max(money))
else:
    while low <= high:
        mid = (high + low) // 2
        k = 0


        for i in money:
            if mid >= i:
                k += i
            else:
                k += mid


        if k <= total_budget:
            low = (mid + 1)
            max_mid = max(max_mid, mid)

        else:
            high = (mid - 1)


    print(max_mid)




