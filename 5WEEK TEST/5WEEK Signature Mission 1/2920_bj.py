ascend = [1, 2, 3, 4, 5, 6, 7, 8]
descend = [8, 7, 6, 5, 4, 3, 2, 1]

list = list(map(int, input().split()))

if list == ascend:
    print('ascending')
elif list == descend:
    print('descending')
else:
    print('mixed')

