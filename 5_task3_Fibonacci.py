

# Find Fibonacci series for a given number

num = int(input("Enter your number : "))

# The values of first two numbers are known

figure1 = 0
figure2 = 1
print("Get Fibonacci seriers :")
# Iterate the numbers up to the given number

for n in range(0, num):
    if n <= 1:
        next = n # When 0 and 1
    else:
        next = figure1 + figure2
        figure1 = figure2
        figure2 = next

    print(next)
