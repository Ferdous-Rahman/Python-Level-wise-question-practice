start = int(input("Enter start range of num: "))
end = int(input("Enter end range of num: "))
print("Numbers divisible by 3 and 5:")
for i in range(start, end+1): 
    if i % 3 ==0 and i % 5 ==0: 
        print(i)