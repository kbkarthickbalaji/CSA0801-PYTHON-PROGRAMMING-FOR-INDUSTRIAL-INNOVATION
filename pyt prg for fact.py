def fact(n):
    if(n==1):
        return 1
    else:
    return*fact(n-1)
n=eval(input("enter the number to find fact:"))
fact=fact(n)
print("fact is",fact)
