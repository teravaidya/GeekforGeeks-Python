# Python program showing how to
# multiple input using split

# taking two inputs at a time
x, y = input("Enter two values: ").split()
print("No. of boys", x)
print("No. of girls", y)
print()

# taking three inputs at a time
x, y, z = input("Enter three inputs: ").split()
print("Total number of students: ", x)
print("Number of boys is : ", y)
print("Number of girls is : ", z)
print()

# taking two inputs at a time
x, y = input("Enter two inputs: ").split()
print("First number is {} and second number is {}".format(x, y))
print()

# taking multiple inputs at a time
# and type casting using list() function
x = list(map(int, input("Enter multiple values: ").split()))
print("List of students:", x)

