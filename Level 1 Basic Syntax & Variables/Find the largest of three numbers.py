numbers = list(map(int,input("Enter as much numbers as you can: ").split()))

numbers.sort(reverse=True)#sorting and reversing the numbers
print(numbers)
print(numbers[:3]) # [:3] will print first 3 number