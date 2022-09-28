

# Test 1 of 3:
print("Test 1:")

message = "Flat is better than nested"
print(message)

# number of 'better', 'never' and 'is' in massage
print("Number of 'better': ",message.count('better'))
print("Number of 'never': ",message.count('never'))
print("Number of 'is': ",message.count('is'))

# trying to convert to uppercase
uppercase_message = message.upper()
print("In uppercase: ",uppercase_message)

# change "i" to "&"
replaced_letter = message.replace("i", "&")
print('Replace "i" and "&": ',replaced_letter)

########################################################

#Test 2 of 3:
print('Test 2:')

# Шукаємо добуток цифр
n = input("Enter four-digit number : ")

n = int(n) # Переводимо str в int

# Define each number
num1 = n%10
num2 = n%100//10
num3 = n%1000//100
num4 = n//1000

print("Multiplying digits in a number ",n," is: ",num1*num2*num3*num4)

################


# Revers order for number
r = input("Enter four-digits number: ")

print("Revers order for ",r," is: ",r[3::-1])


# Посортувати цифри

print('Sort numbers in ',r,' is: ',sorted(r))


#####################################################

# Test 3 of 3:
print("Test 3:")

# Change value for a and b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))


print("a = ",a)
print("b = ",b)

print("Will change value between A and B:")
(a, b) = (b, a) # Changing value

print('(a, b) = (b, a)')
print("Value of 'a' changed to: ",a)
print("And value of 'b' changed to: ",b)
