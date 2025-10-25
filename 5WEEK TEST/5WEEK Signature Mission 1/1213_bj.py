#메모리초과

# from itertools import permutations
# li = list(input().rstrip())
# alpha = set()
#
# for i in permutations(li, len(li)):
#     alpha.add(''.join(i))
#
# alpha = sorted(alpha)
# half = len(li) // 2
#
#
# #짝수면
# if len(li) % 2 == 0:
#
#     for i in alpha:
#         half = len(i) // 2
#
#         if i[0:half] == i[half:][::-1]:
#             print(i)
#             break
#     else:
#         print("I'm Sorry Hansoo")
#
# #홀수면
# else:
#     for i in alpha:
#         half = len(i) // 2
#
#         if i[0:half] == i[half+1:][::-1]:
#             print(i)
#             break
#     else:
#         print("I'm Sorry Hansoo")


