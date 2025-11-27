num = int(input("Enter a number: "))

sum = 0

while num >0:
    last_digit = num%10  # for go to the last digit
    sum = sum + last_digit
    num //= 10 # removing last digit

print("Sum of digits =", sum)