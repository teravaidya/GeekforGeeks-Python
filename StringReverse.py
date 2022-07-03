# Program to reverse a string
gfg = "GeekForGeeks"
print(gfg[::-1])

# Palindrome check
string1 = "Malayalam"
reverse = string1[::-1]
if string1.lower() != reverse.lower():
  print("Its not")
else:
  print("It's palindrome")

# Program to reverse a string
gfg = "GeekForGeeks"

# Reverse the string using reversed and join function
gfg = "".join(reversed(gfg))
print(gfg)
