def value_num(n):
    if (n==0):
        return
    print(n)
    value_num(n-1)
    print("end")

value_num(10)    