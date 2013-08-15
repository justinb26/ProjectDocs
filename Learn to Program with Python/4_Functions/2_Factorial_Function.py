## Computes a factorial, using a recursive function (a function that calls itself)

def factorial(x):
  if x == 0:
    return 1
  else:
    return x * factorial(x-1)

print(factorial(6))