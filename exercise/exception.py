try:
    num = int(input("Enter a number: "))
    print(10/num)
except ValueError:
    print("Invalid number!")
except ZeroDivisionError:
    print("Can't divide by zero!")
finally:
    print("Operation complete")
    