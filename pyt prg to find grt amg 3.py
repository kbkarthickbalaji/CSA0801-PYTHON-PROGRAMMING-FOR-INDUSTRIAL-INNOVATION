a = eval(input("Enter a value of a: "))
b = eval(input("Enter a value of b: "))
c = eval(input("Enter a value of c: "))

if a > b:
    if a > c:
        print("The greatest number is", a)
    else:
        print("The greatest number is", c)
elif b > c:
    print("The greatest number is", b)
else:
    print("The greatest number is", c)
