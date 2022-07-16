# Python program to demonstrate Keyword Arguments
def student(firstname, lastname):
  print(firstname, lastname)


# Keyword arguments
if __name__ == "__main__":
  student(firstname='Geeks', lastname='Practice')
  student(lastname='Practice', firstname='Geeks')
