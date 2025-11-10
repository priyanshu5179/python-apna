def pattern(n):
    if(n==0):
       return
    print("*"*n)
    pattern(n-1)#this is calling function itsef
pattern(3)    