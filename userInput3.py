# Input multiple values from user in one line

x, y = input(), input()
print("x = ", x, "y = ", y)

# use of split() - whitespace is the default delimiter
x, y = input().split()

# Type cast string to integer
x, y = [int(x), int(y)]
print(x, y)

