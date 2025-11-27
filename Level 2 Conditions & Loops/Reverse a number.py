num = int(input("Enter a number: "))

rev = 0

while num >0:
    digit = num%10  # for go to the last digit
    rev = rev * 10 + digit
    num //= 10 # removing last digit

print("reversed =", rev)