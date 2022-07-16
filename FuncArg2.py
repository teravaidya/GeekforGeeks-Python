# Python program to demonstrate
# default arguments


def myFun(x, y=50):
  print("x: ", x)
  print("y: ", y)


# Driver code (We call myFun() with only
# argument)
if __name__ == "__main__":
  myFun(10)
