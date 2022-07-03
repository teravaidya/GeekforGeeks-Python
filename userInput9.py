
# Python program showing
# how to take multiple input
# using List comprehension

# taking two input at a time
x, y = [int(num) for num in input("Enter 2 values: ").split()]
print("First Number is: ", x)
print("Second Number is: ", y)
print()

# taking three input at a time
x, y, z = [int(num) for num in input("Enter 3 values: ").split()]
print("First Number is: ", x)
print("Second Number is: ", y)
print("Third Number is: ", y)
print()

# taking two inputs at a time
x, y = [int(num) for num in input("Enter 2 values: ").split()]
print("First number is {} and second number is {}". format(x, y))
print()

# taking multiple inputs at a time
x = [int(num) for num in input("Enter multiple values: ").split()]
print("Number of list is: ", x)

# taking multiple inputs at a time separated by comma
x = [int(num) for num in input("Enter multiple values: ").split(',')]
print("Number of list is: ", x)
