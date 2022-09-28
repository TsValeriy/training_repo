

# inpun number to calculate the factorial

n = input("Enter number: ")

fact = 1

if int(n) >= 1: # type n changed to int


# calculate factorial in number from number 1 to n+1
    for i in range(1, int(n)+1):
        fact = fact*i

print("Factorial of ",n," is: ",fact)
