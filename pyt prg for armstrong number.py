n = eval(input("Enter a number: "))
org = n  
sum = 0
while n > 0:
    a = n % 10
    sum = sum + a * a * a
    n = n // 10
if sum == org:
    print("The given number is an Armstrong number")
else:
    print("The given number is not an Armstrong number")
