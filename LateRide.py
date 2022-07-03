import math


def solution(n):
  sum = 0
  if n < 10:
    return n
  hours = math.floor(n / 60)
  mins = n - hours * 60

  for digit in str(hours):
    sum += int(digit)

  for digit in str(mins):
    sum += int(digit)
  return sum


if __name__ == '__main__':
  sum = solution(240)
  print(sum)
