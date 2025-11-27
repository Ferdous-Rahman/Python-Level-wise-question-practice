

n = int(input("Enter number of rows: "))

for i in range (1,n+1):
    print(" "*(n-i)+"*"*(2*i-1))


# For row i:

# Left spaces = n - i

# Stars = 2*i - 1

# Stars increase like: 1, 3, 5, 7...