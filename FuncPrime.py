# some more functions

def isPrime(n: int) -> bool:
  if n in [2, 3]:
    return True
  if n % 2 == 0:
    return False
  r = 3
  while r * r <= n:
    if n % r == 0:
      return False
    r += 2
  return True


if __name__ == "__main__":
  print(isPrime(78), isPrime(79))
