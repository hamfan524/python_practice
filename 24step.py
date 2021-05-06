#피보나치 수열
#f(n) = f(n-1) + f(n-2)

counter = 0

def f(n):
  global counter
  counter += 1
  if (n == 1 or n == 2):
    return 1
  else:
    return f(n - 1) + f(n - 2)

print("{}".format(f(100)))
print("{}번 반복".format(counter))   