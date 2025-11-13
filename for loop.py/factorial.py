n=int(input("enter a number"))
product=1
for i in range(1 ,n+1):
    product*=i
    print(f"factorial{n} is{product}")