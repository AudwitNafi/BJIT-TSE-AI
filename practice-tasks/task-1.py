def calcMaxAbsDiff(numbers, n):
    numbers.sort()
    return numbers[n-1] - numbers[0]

n = int(input("Enter number of elements: "))
numbers = []
i = 0
print(f"Enter the {n} elements one in each line:")
while i < n:
    x = input()
    if x.lstrip('-+').isdigit():
        x = int(x)
        numbers.append(x)
        i+=1
    else:
        print("Invalid number!")
print(numbers)
print(f"The absolute max difference: {calcMaxAbsDiff(numbers, n)}")