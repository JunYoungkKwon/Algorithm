T = int(input())
for _ in range(T):
    cnt_left = 0
    test = input()
    for a in test:

        if a == "(":
            cnt_left += 1
            if cnt_left >= len(test):
                print("NO")
                break
        elif a == ")":
            cnt_left += -1
            if  cnt_left < 0:
                print("NO")
                break
    else:
        if cnt_left == 0:
            print("YES")
        else:
            print("NO")

