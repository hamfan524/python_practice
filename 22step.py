# start~end까지 있는 모든 정수를 더하는 함수

def sum_all(start, end):
  a = 0
  for i in range(start, end +1):
    a += i
  return a

print(sum_all(1, 100))
print(sum_all(50, 100))

#x를 반환하는 방정식
def f(x):
  x = (x ** 2) + (x * 2) + 1 
  return x

print(f(10))


#가변 매개변수의 값을 두 곱해서 반환
def mul(*values):
  a = 1
  for i in values:
    a *= i
  return a

print(mul(5, 7, 9, 10))