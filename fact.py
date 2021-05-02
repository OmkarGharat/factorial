'''
To find whether a given number is a factorial number or not. If it is not a factorial number then print
the largest factorial number less than the given number and smallest factorial number greater than the given number.
'''

n = int(input("Enter a number : "))

if n == 0 :
    print(n,"is not factorial of any number")
elif n < 0 :
    print("factorial of negative numbers does not exists")
elif n == 1 :
    print(n,"is factorail of 0 and 1")
else :
    y = 1
    i = 1
    while i < n + 1 :
        y = y * i
        if y == n :
            print(n,"is factorial of",i)
            break
        if y > n :
            f = y // i
            print(n,"is not factorial of any number")
            print(f,"is smallest factorial number less than",n)
            print(y,"is largest factorial number greater than",n)
            break
        i = i + 1
