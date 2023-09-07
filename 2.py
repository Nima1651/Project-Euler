sum = 0
num1 = 0
num2 = 1
next_number = num2



while sum < 4000000:
    num1, num2 = num2, next_number
    next_number = num2 + num1
    if next_number % 2 == 0:
        sum += next_number


print(sum)