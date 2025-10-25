
money = (1000 - int(input()))

if money == 0:
    print(0)
else:
    a = money // 500
    b_money = (money % 500)
    b = b_money // 100
    c_money = (b_money % 100)
    c = c_money // 50
    d_money = (c_money % 50)
    d = d_money // 10
    e_money = (d_money % 10)
    e = e_money // 5
    f_money = (e_money % 5)
    f = f_money // 1
    print(a+b+c+d+e+f)






