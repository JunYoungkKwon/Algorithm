money = int(input())
money = 1000 - money
chg = [500, 100, 50, 10, 5, 1]
ans = 0
if money:
    for ch in chg:
        ans += (money // ch)
        money %= ch

    print(ans)

else:
    print(ans)
