def fac(num):
    result = 1
    if num > 0:
        result = num * fac(num-1)
    return result

n = int(input())
print(fac(n))