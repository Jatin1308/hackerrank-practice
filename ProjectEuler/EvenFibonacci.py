def evenFibonacci(n):
    a = 0
    b = 1
    c = a+b
    op = 0
    def res(n,a,b,c,op):
        print(n,a,b,c,op)
        if c > n:
            print("Inside")
            return op
        
        # calculating fibonacci numbers 
        a,b = b,c
        c = a+b

        # calculating op to be returned if even number
        if(c%2==0 and c<n):
            op+=c
        return res(n,a,b,c,op)

    return res(n,a,b,c,op)

        



print("Final Op: ",evenFibonacci(100))