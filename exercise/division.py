def divide(x, y):
    try:
        res = x/y
        print(f"The division is sucessful. The result is: {res}")
    except ValueError:
        print("Invalid values for x and y")
    except ZeroDivisionError:
        print("Cannot divide by zero")
    finally:
        print("Division complete")

x = int(input("Input first Number: "))
y = int(input("Input second Number: "))

divide(x, y)