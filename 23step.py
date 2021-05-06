#팩토리얼 문제 - 단순 반복문과 재귀함수 사용
#n! = 1 * 2 * 3 * ... * (n-2) * (n-1) * n

def factorial_1(n, a = 1):
  for i in range(1, n + 1):
    a *= i  

  return a

print(factorial_1(3))




#n! = n * (n-1)!
#0! = 1

def factorial_2(n):
  if n == 0:
    return 1
  else:
    return n * factorial_2(n - 1)

print(factorial_2(10))