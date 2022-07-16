# Python program to illustrate
# *kwargs for variable number of keyword arguments


def myFun(**kwargs):
  for key, value in kwargs.items():
    print("%s == %s" % (key, value))


# Driver code
if __name__ == "__main__":
  myFun(first='Geeks', mid='for', last='Geeks')
