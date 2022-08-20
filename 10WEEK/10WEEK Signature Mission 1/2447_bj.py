def draw_stars(n):
  if n==1:
    return ['*']

  Stars=draw_stars(n//3)
  L=[]

  for star in Stars:
    L.append(star*3)
  for star in Stars:
    L.append(star+' '*(n//3)+star)
  for star in Stars:
    L.append(star*3)

  return L

N=int(input())
print('\n'.join(draw_stars(N)))
#기본 패턴
# N = int(input())
# ans1 = "***"
# ans2 = "* *"
# ans3 = "***"
# def cursion(i):
#     global ans1, ans2, ans3
#
#     if 3**i == N:
#         print(ans1)
#         print(ans2)
#         print(ans3)
#     else:
#         for _ in range(3):
#             ans1 *= 3
#             ans2 *= 3
#             ans3 *= 3
#         cursion(i+1)
# cursion(1)