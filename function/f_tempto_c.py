def f_to_c(f):
    c = (f - 32) * 5/9
    return c

f = float(input("Enter temperature in Fahrenheit: "))
print("Temperature in Celsius:", f_to_c(f))
