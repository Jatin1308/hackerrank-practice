def multiple3or5(n):

    # timeout
    # return sum(range(0,n,3)) + sum(range(0,n,5)) - sum(range(0,n,15))

    # timeout
    # s = 0
    # for i in range(1,n):
    #     if i%3 == 0 or i%5==0:
    #         s+=i
    # return s

    # timeout
    # op = lambda n: sum(i for i in range(1, n) if i % 3 == 0 or i % 5 == 0)
    # return op(n)


    max3 = range(0, n, 3)[-1]  # get the maximum number divisble by 3
    max5 = range(0, n, 5)[-1]  # get the maximum number divisble by 5
    max15 = range(0, n, 15)[-1] # get the maximum number divisble by 15 

    print(max3,max5,max15)

    sum3 = (max3 + 3) * max3 // 3 // 2
    sum5 = (max5 + 5) * max5 // 5 // 2
    sum15 = (max15 + 15) * max15 // 15 // 2

    print(sum3,sum5,sum15)

    return sum3+sum5-sum15

print(multiple3or5(100))

