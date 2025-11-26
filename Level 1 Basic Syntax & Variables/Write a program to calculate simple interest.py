# Simple interest, I = (Prn)/100 . where P= principle, r = rate in 100%, n = time

p = int(input("Enter principle: "))
r = float(input("Enter rate: "))
n = int(input("Enter time (in year): "))

SI = (p*r*n)/100
print(SI)