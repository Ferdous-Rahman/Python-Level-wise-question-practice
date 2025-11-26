numbers = list(map(int,input("Enter as much numbers as you can: ").split()))
#map() is a built-in function that applies another function to every item of an iterable (like a list, string, or input split).

total =sum(numbers) #sum() for adding multiple numbers  

print(numbers)
print(total)