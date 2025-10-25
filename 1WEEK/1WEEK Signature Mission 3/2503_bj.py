from itertools import permutations
N = int(input())
case = list(permutations([1,2,3,4,5,6,7,8,9], 3))
print(case)
for _ in range(N):
    num, s , b = map(int, input().split())
    rmvNum = 0
    num =list(str(num))
    for i in range(len(case)):
        sNum = bNum = 0
        i -= rmvNum

        for j in range(3):

            if case[i][j] == num[j]:
                sNum += 1
            elif num[j] in case[i]:
                bNum += 1
        if sNum != s or bNum != b:
            case.remove(case[i])
            rmvNum += 1
print(len(case))
