def sum_mul(n, m):
    contador=0
    num = 1
    if (m <= 0):
        print('INVALID')
    else:
        for num in range(n,m):
            try:
                if num % n == 0:
                    contador +=num
            except ZeroDivisionError:
                print('INVALID')
    print(contador)
    return contador

sum_mul(2, 9)
sum_mul(3, 13)
sum_mul(4, 123)
sum_mul(4, -7)
sum_mul(0, 0)